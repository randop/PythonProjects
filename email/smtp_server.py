import asyncio
import time
import datetime
from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        print('Message from',envelope.mail_from)
        print('Message for',envelope.rcpt_tos)
        print('Message data:\n')
        print(envelope.content.decode('utf8', errors='replace'))
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
