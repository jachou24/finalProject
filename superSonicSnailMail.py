import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

# Email credentials
smtp_server = "smtp.gmail.com"  # For Gmail
port = 587  # SMTP port for TLS
sender_email = "jmchou@umass.edu"  # Your email
app_password = "hkuv yikz hzza muqd "  # Use the generated App Password
subject = "Photobooth"

def sendEmail(imgName, receiver_email):
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = subject
  image_path = imgName

  with open(image_path, 'rb') as img:
      msg_img = MIMEImage(img.read(), name=os.path.basename(image_path))
      message.attach(msg_img)

  with smtplib.SMTP(smtp_server, port) as server:
      server.starttls()
      server.login(sender_email, app_password)
      server.send_message(message)
      print("Email sent successfully!")