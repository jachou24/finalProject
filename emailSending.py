import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os

# Email credentials
smtp_server = "smtp.gmail.com"  # For Gmail
port = 587  # SMTP port for TLS
sender_email = "jmchou@umass.edu"  # Your email
app_password = "hkuv yikz hzza muqd "  # Use the generated App Password
receiver_email = input("Please enter your email:")  # Recipient's email

# Create the email content
subject = "Photobooth"
body = "Excellent photo! Here it is:\n"

# Construct email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

image_path = 'smile.jpg'

html = """\
<html>
  <body>
    <p>Hi,<br>
    Here is your photo: <img src="cid:image1">.</p>
  </body>
</html>
"""
with open(image_path, 'rb') as img:
    # Attach the image file
    msg_img = MIMEImage(img.read(), name=os.path.basename(image_path))
    # Define the Content-ID header to use in the HTML body
    msg_img.add_header('Content-ID', '<image1>')
    # Attach the image to the message
    message.attach(msg_img)

# Send email
try:
    # Establish connection to SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Upgrade connection to secure TLS
        server.login(sender_email, app_password)  # Log in using the App Password
        server.send_message(message)  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
