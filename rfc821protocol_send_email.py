
import smtplib, ssl
import getpass




port_number = 465

smtp_server = "smtp.gmail.com"

sender = "my@gmail.com"

reciever = "to@gmail.com"

password = getpass.getpass()

cont = ssl.create_default_context()


with open("D:\pycharm/test.txt", "r") as file:
        
    message = file.read()
        
    file.close()

try:

    with smtplib.SMTP_SSL(smtp_server, port = port_number, context = cont) as server:
    
        server.login(sender_email, password)
    
        server.sendmail(sender_email, reciever_email, message)

except SMTPException:
    
    print("Error !!!")