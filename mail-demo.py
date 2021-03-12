# 1. Place passwords in environment variable
import os
# connect to mail server
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out this room '
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'bettymukami98@gmail.com'
msg.set_content('Image attached..')

files = ['sasha-stories-qzt0DKKG8Pc-unsplash.jpg', 'saad-khan-425b2PhNuHA-unsplash.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to our mail server

    smtp.send_message(msg)