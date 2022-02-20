from array import array
import smtplib
from email.message import EmailMessage

from typing import List

from django.conf import settings


def send_email(subject: str, to: List[str], content: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_ADDRESS
    msg["To"] = ", ".join(to)
    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)

        smtp.send_message(msg)
