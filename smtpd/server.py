import asyncio
import time
import datetime
from aiosmtpd.controller import Controller
import email

from pprint import pprint
from pprint import saferepr
from inspect import getmembers

class CustomHandler:
    async def handle_exception(self, error):
        print('Server Error:')
        print(saferepr(error))
        return '500 Internal server error'

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        post = {}
        msg = email.message_from_bytes(envelope.content)
        print(saferepr(msg))
        if 'message-id' in msg:
            print('Message-ID:', msg['message-id'])
        post['headers'] = dict(msg.items())
        for part in msg.walk():
            if part.get_content_type()=='text/plain' and not bool(post.get('plain')):
                post['plain'] = part.get_payload()
            if part.get_content_type()=='text/html' and not bool(post.get('html')):
                post['html'] = part.get_payload()
            if not part.get_content_disposition() is None:
                with open('/tmp/file.jpg', 'wb') as f:
                    f.write(part.get_payload(i=None, decode=True))
                
        print(saferepr(post))
        return '250 Message accepted for delivery'

controller = Controller(CustomHandler(), None, '0.0.0.0', 8025)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print('Running SMTP Server ', st)

controller.start()

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    controller.stop()
    loop.close()
