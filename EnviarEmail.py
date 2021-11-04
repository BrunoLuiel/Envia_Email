# https://www.youtube.com/watch?v=umvzsQLZYD4
#Ver o erro que está dando, parei em 19:54


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Para anexar arquivos - Necessário pois o arquivo é enviado de forma binaria, ou seja há necessidade de converter
from email.mime.base import MIMEBase
from email import encoders


#Simple Mail Transfer Protocol
#Para criar o servidor e enviar o e-mail

#1 - Startar o servidor SMTP

host = "smtp.gmail.com" #Estes dados são encontrados no site do google ou na própria configuração do Gmail
port = "587"
login = "Seuemail@gmail.com"
senha = "Sua senha"

server = smtplib.SMTP(host,port)

server.ehlo()#Comandos para indicar que estou iniciando os servidor
server.starttls() #Ainda assim quando der erro é porque deve abrir o gmail no chrome, ir em cofiguração/segurança/'Acesso app menos seguros' e clicar em permitir

server.login(login,senha)

#2 - Construir o e-mail tipo MIME

titulo_email = "Olá, tudo bem?"
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['to'] = 'fiscal@ji-paranacontabilidade.com.br'
email_msg['Subject'] = 'Meu e-mail enviado'
email_msg.attach(MIMEText(titulo_email, 'plain')) #Posso experimentar alterar 'plain' por 'HTML'

##Anexar arquivo:
# Abrimos o arquivo em modo leitura e binary
caminho_arq = 'C:\\Users\\ADM\\Downloads\\51210200018641279881559250000000171086066661-nfe.pdf'# neste paragrafo o arquivo é lido
arquivo = open(caminho_arq, 'rb')

#Leitura do arquivo em modo binario e codificado em base 64 (que é o que o e-mail precisa)
arq = MIMEBase('application', 'octet-stream')#neste paragrafo o arquivo é transformado em base64 (binario)
arq.set_payload(arquivo.read())
encoders.encode_base64(arq)

#Adicionamos o cabeçalho no tipo anexo e-mail
arq.add_header('Content-Disposition', f'attachment; filename= EnviaEmail.py') #Ou para variável insira "{nomedavariavel}"
#Fechamos o arquivo
# arquivo.close()

#Inseri o anexo ao corpo do e-mail
email_msg.attach(arq)


#3 - Enviar o e-mail  tipo MIME no servidor

server.sendmail(email_msg['From'], email_msg['to'], email_msg.as_string())
server.quit()
