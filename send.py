import base64
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_pubsub(event, context):
    if 'data' in event:
        mail_content = base64.b64decode(event['data']).decode('utf-8')
    else:
        mail_content = "Error"
    #The mail addresses and password
    sender_address = os.environ.get("SERVER_EMAIL")
    sender_pass = os.environ.get("SERVER_PASS")
    receiver_address = os.environ.get("MY_EMAIL")
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'My Subject'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
