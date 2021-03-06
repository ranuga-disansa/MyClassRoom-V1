import smtplib
import smtpd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(to_email,subject,body):
    msg = MIMEMultipart()
    msg['From'] = "go2ranuga@gmail.com"
    msg['To'] = to_email
    msg['subject'] = subject
    msg['Body'] = body
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login()
        server.sendmail("", to_email, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(" Something went wrong...." + str(e))
        return False
