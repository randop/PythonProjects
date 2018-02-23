import smtpd
import asyncore

print('here')

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))

server = CustomSMTPServer(('0.0.0.0', 1025), None)

print('Starting server:')
asyncore.loop()

