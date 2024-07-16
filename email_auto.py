from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('pass', 'r').read()
email_origem = 'mateus@maxbot.com.br'
email_destino = ('mts.horta@gmail.com', 'teu_ziim@hotmail.com')

assunto = 'Documentos de Regularidade Maxbot'

body = open('body-teste.txt', 'r').read()