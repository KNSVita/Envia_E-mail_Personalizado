import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#configurando servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
#e-mail do remetente
smtp_username = 'videoweb@anchietaba.com.br'
#senha do e-mail do remetente
smtp_password = 'ctpstp2019'

destinatarios = [
    {'nome':'Kauan','senha':'testesenha','email':'kauanvita@gmail.com'}
]

#Corpo do e-mail
assunto = 'Login para acesso'
mensagem = '''
Olá {nome},

Segue usuário e senha para acesso:


'''
server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(smtp_username,smtp_password)

#Envio dos e-mails
for destinatario in destinatarios:
    nome = destinatario['nome']
    email = destinatario['email']

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = assunto

    corpo_email = mensagem.format(nome=nome)
    msg.attach(MIMEText(corpo_email,'plain'))

    server.sendmail(smtp_username,email,msg.as_string())
    print(f'E-mail enviado para {email}')

server.quit()

print('Envio finalizado')