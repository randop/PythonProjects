import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com')) + ', ' + email.utils.formataddr(('Test',
                                    'test@example.com'))
print(msg['To'])
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

#server = smtplib.SMTP('192.168.99.100', 1025)
server = smtplib.SMTP('127.0.0.1', 8025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com', 'test@exmple.com'],
                    msg.as_string())
finally:
    server.quit()