import smtplib
import ssl
from email.message import EmailMessage
f

# User configuration
def send_email(nombre, correo, mensaje):

    sender_email = 'emailbottle@gmail.com'
    receiver_email = 'ogobillon@gmail.com'
    password = 'e7121941'
    cuerpo = '''
    NOMBRE: {}
    EMAIL: {}
    MSG:
    {}'''.format(nombre,correo,mensaje)

    msg = EmailMessage()
    msg.set_content(cuerpo)

    msg['Subject'] = 'serti pythonanywhere'
    msg['From'] = sender_email
    msg['To'] = receiver_email




    # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Encrypts the email
    context = ssl.create_default_context()
    server.starttls(context=context)
    # We log in into our Google account
    sesion = server.login(sender_email, password)
    # Sending email from sender, to receiver with the email body
    envios = server.send_message(msg)
    # print('Email sent!')

    # print('Closing the server...')
    server.quit()



    return None

