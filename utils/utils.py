import smtplib
from email.mime.text import MIMEText
from .config import SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_RECEIVER

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