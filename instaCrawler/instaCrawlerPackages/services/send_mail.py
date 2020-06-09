import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import json

def load_mail_data(json_path):
    try:
        print("loading mail data")
        with open(json_path, 'r') as f:
            mail_data = f.read()
            mail_data = json.loads(mail_data)
            print("mail data loaded")
            return mail_data
    except Exception as e:
        print(e)

load_mail_data("")

def create_message(mail_data):
    try:
        print("creating message")
        msg = MIMEMultipart()
        msg['From'] = mail_data["from"]
        msg['To'] = mail_data["to"]
        msg['Subject'] = mail_data["Subject"]
        body = open(mail_data["body"], 'r').read()
        msg.attach(MIMEText(body, 'html'))
        filename = os.path.basename(mail_data["file"])
        attachment = open(mail_data["file"], "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        print("message created")
        return msg
    except Exception as e:
        print(e)


def send_mail(mail_data):
    try:
        # mail_data = load_mail_data(json_path)
        msg = create_message(mail_data)
        print("trying to send mail ....")
        server = smtplib.SMTP(mail_data["mail_server"], 587)
        server.starttls()
        server.login(mail_data["from"], mail_data["password"])
        text = msg.as_string()
        server.sendmail(mail_data["from"], mail_data["to"].split(","), text)
        server.quit()
        print("mail sent")
    except Exception as e:
        print(e)
