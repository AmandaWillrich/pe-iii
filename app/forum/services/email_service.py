import smtplib, ssl
from pathlib import os


class EmailService:
    
    def __init__(self, port=None, smtp_server=None, sender_email=None, sender_password=None, receiver_email=None):
        self.port = port or 465
        self.smtp_server = smtp_server or 'smtp.gmail.com'
        self.sender_email = sender_email or str(os.getenv('DEVELOPMENT_EMAIL'))
        self.sender_password = sender_password or str(os.getenv('DEVELOPMENT_EMAIL_PASSWORD'))
        self.receiver_email = receiver_email or str(os.getenv('DEVELOPMENT_EMAIL'))


    def send(self, fullname, subject, email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.sender_password)

            server.sendmail(
                self.sender_email,
                self.receiver_email,
                self.create_message_body(fullname, subject, email, message)
            )

    def create_message_body(self, fullname, subject, email, message):
        return (f'''######################### FORMULÁRIO DE CONTATO #########################\n
            Enviada por: {fullname}\n
            Email: {email}\n
            Assunto: {subject}\n\n
            Mensagem: {message}\n
            ######################### FIM FORMULÁRIO DE CONTATO #########################
        ''').encode('utf-8', 'ignore')
