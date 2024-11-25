import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

# Email credentials
smtp_server = "smtp.gmail.com"  # For Gmail
port = 587  # SMTP port for TLS
sender = "jmchou@umass.edu"  # Your email
appPass = "hkuv yikz hzza muqd "  # Use the generated App Password
subject = "Photobooth"

def sendEmail(imgName, receiver):
  message = MIMEMultipart()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = subject

  with open(imgName, 'rb') as img:
      msgImg = MIMEImage(img.read(), name=os.path.basename(imgName))
      message.attach(msgImg)

  with smtplib.SMTP(smtp_server, port) as server:
      server.starttls()
      server.login(sender, appPass)
      server.send_message(message)
      print("Email sent successfully!")