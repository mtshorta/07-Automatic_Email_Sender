from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('pass mateus@maxb', 'r').read()
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


# anexo_path = '/Users/mateushorta/Desktop/NFSE-secult.pdf'
# mimetype, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')

# with open(anexo_path, 'rb') as ap:
#     mensagem.add_attachment(ap.read(), maintype=mimetype, subtype=mime_subtype, 
#                             filename= anexo_path.split('/')[-1]) #quebro o path e pego o último valor da lista quebrada nas '/'
    
#
#
#
#
# Here we're setting the attatchmamnt files
folder = ('/Users/mateushorta/Desktop/03-MAXbot/7 - Documentos Ther Sistemas Inovadores/Documentos legais comprobatorios')
patterns = ['1-THERIONTEC', '2-THERIONTEC', '3-THERIONTEC', '4-THERIONTEC', '5-THERIONTEC']

#Creating a list with the paths of the files we need to attatch in documentos de regularidade
files = []
for file in os.listdir(folder):
    for pattern in patterns:
        if pattern in file:
            files.append(os.path.join(folder,file))
#Creating a list with the paths of the files we need to attatch in desktop, NFSes
folder2 = ('/Users/mateushorta/Desktop')
patterns2 = ['SECULT', 'secult', 'Secult']

for file in os.listdir(folder2):
    for pattern in patterns2:
        if pattern in file:
            files.append(os.path.join(folder2,file))
#Attatching the files
for file_path in files:
    with open(file_path, 'rb') as ap:
        mime_type, mime_subtype = mimetypes.guess_type(file)[0].split('/')
        mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, 
                                filename=file_path.split('/')[-1])


#smtp.gmail.com é o smtp, se o da maxbot for outro terei que trocar.
#o 465 é a porta
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
