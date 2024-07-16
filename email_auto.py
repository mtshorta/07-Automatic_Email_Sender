from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('pass mateus@max', 'r').read()
email_origem = 'mateus@maxbot.com.br'
email_destino = ('mts.horta@gmail.com', 'teu_ziim@hotmail.com')
email_copia = ('julinhafpadrao@hotmail.com')

assunto = 'Documentos de Regularidade Maxbot'

body = open('body-teste.txt', 'r').read()

mensagem = EmailMessage()

mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto
mensagem['Cc'] = email_copia

mensagem.set_content(body)
safe = ssl.create_default_context()


anexo_path = '/Users/mateushorta/Desktop/NFSE-secult.pdf'
mimetype, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')

with open(anexo_path, 'rb') as ap:
    mensagem.add_attachment(ap.read(), maintype=mimetype, subtype=mime_subtype, 
                            filename= anexo_path.split('/')[-1]) #quebro o path e pego o último valor da lista quebrada nas '/'
    


#smtp.gmail.com é o smtp, se o da maxbot for outro terei que trocar.
#o 465 é a porta
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
