import smtplib
from email.message import EmailMessage
sender_email = "sumanpone8@gmail.com"
receiver_email = "srimanyuacharya@gmail.com"
app_password = "zbhh aspc lmki imds"
# Create the email
msg = EmailMessage()
msg.set_content("Hello! This email was sent using Python.")
msg["Subject"] = "Test Email"
msg["From"] = "sumanpone8@gmail.com"
msg["To"] = "srimanyuacharya@gmail.com"

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()               # Secure the connection
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent!")
