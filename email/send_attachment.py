import smtplib
import email.utils
import time
import datetime
import mimetypes

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from email.MIMEBase import MIMEBase

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

msg = MIMEMultipart('alternative')
msg['Subject'] = "TEST ONLY " + st
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
msg['Cc'] = email.utils.formataddr(('Recipient', 'test@example.com'))
msg['Bcc'] = email.utils.formataddr(('Recipient', 'test@example.com'))
msg['X-Mailer'] = "test"

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    <small>%s</small>
  </body>
</html>
""" % (st)

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

filename1 = "computer.jpg"
mime = mimetypes.guess_type(filename1)
mime = mime[0].split('/')

attachment1 = MIMEBase(mime[0], mime[1])
attachment1.set_payload(open(filename1, "rb").read())
Encoders.encode_base64(attachment1)
attachment1.add_header('Content-Disposition', 'attachment; filename=' + filename1)

msg.attach(part1)
msg.attach(part2)
msg.attach(attachment1)

#server = smtplib.SMTP('192.168.99.100', 1025)
server = smtplib.SMTP('127.0.0.1', 8025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()