import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from .config import SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_RECEIVER
import africastalking
import os

from schemas import project_schemas

# Africa's Talking setup
africastalking.initialize(username="sandbox", api_key="your_api_key")  # Replace with live credentials
sms = africastalking.SMS


def send_contact_email(name: str, email: str, message:str) -> None:
    subject = f"New Contact Form Submission from {name}"
    body = f"""
    You received a new message from your website:

    Name: {name}
    Email: {email}

    Message:
    {message}
    """
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg['From'] = email
    msg['To'] = EMAIL_RECEIVER
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg=msg)
    except Exception as e:
        print(f"Error sending email: {e}")
        raise(e)
    


def send_email(hire: project_schemas.HireCreate):
    msg = EmailMessage()
    msg['Subject'] = f"Hire Request: {hire.subject}"
    msg['From'] = os.getenv("SMTP_USER")  # e.g., 'yourmail@example.com'
    msg['To'] = os.getenv("SMTP_RECEIVER")  # e.g., 'yourmail@example.com'
    msg.set_content(f"""
    New Hire Request:

    Name: {hire.name}
    Email: {hire.email}
    Phone: {hire.phone}
    Subject: {hire.subject}

    Description:
    {hire.description}
    """)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        smtp.send_message(msg)

def send_sms(phone: str, message: str):
    response = sms.send(message, [phone])
    print("SMS Response:", response)
