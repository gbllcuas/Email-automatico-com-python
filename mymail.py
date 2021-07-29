u'\u2013'.encode('ascii', 'ignore')
import smtplib #Definição para protocolo de encript host,port

from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders


#SMTP - Simple mail transfer proocol
#Servidor do email

#1-iniciar o servidor smtp

host = "smtp.gmail.com"
port = "587"
login = "xxxxxxxxx"
login2 = "xxxxxxx"
login3 = "xxxxxxx"

senha = "xxxxxxxxxx"



smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(login, senha)

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()

server.login(login,senha)

 
#2- construir email tipo mime

corpo = "Por esse teste venho confirmar script feito em .py"
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = login2

email_msg['From'] = login
email_msg['To'] = login

email_msg['From'] = login
email_msg['To'] = login3





#sub titulo

email_msg['Subject'] = "E-mail enviado "
email_msg.attach(MIMEText(corpo,'plain'))


#abrir arquivo e ler , para o processo de encriptação
cam_arquivo = "C:\\Users\\55929\\Documents\\testepythonenviaremail.txt"
attachment= open(cam_arquivo,'rb')


#transformar arquivo em base binaria 64bits para envio
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)


att.add_header('Content-Disposition','fattachment;filename=testepythonenviaremail.txt')
attachment.close()
email_msg.attach(att)

server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())


server.quit()




