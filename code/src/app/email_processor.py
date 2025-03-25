import imaplib
import email
from email import policy
import pdfplumber
import json

# Load configuration
with open("app/config.json", "r") as config_file:
    config = json.load(config_file)

EMAIL_HOST = config["email_host"]
EMAIL_USER = config["email_user"]
EMAIL_PASS = config["email_pass"]

def fetch_latest_email():
    mail = imaplib.IMAP4_SSL(EMAIL_HOST)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    email_ids = data[0].split()
    latest_email_id = email_ids[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    mail.logout()
    return email.message_from_bytes(raw_email, policy=policy.default)

def extract_email_content(email_msg):
    email_body = email_msg.get_body(preferencelist=("plain"))
    email_text = email_body.get_content() if email_body else "(No text content available)"
    attachments = []
    
    for part in email_msg.iter_attachments():
        if part.get_content_type() == "application/pdf":
            with pdfplumber.open(part.get_payload(decode=True)) as pdf:
                pdf_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
                attachments.append(pdf_text)
    
    return email_text, "\n".join(attachments)
