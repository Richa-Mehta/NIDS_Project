import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver email
sender_email = "sender@gmail.com"
receiver_email = "reciever@gmail.com"
password = "app password"

# Read alerts file
with open("alerts.txt", "r") as file:
    alert_data = file.read()

# Create email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "🚨 Network Alert - Suspicious Traffic Detected"

body = f"""
Hello Admin,

Your NIDS system detected unusual traffic or repeated packet patterns.

Here are the details:

{alert_data}

Please check immediately.

Regards,
Your Network Security System 🕵️‍♀️
"""
msg.attach(MIMEText(body, 'plain'))

# Send email via Gmail SMTP
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    print("✅ Email alert sent successfully!")
except Exception as e:
    print("❌ Error sending email:", e)
