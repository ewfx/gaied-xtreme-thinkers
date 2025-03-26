import openai
import re
import imaplib
import email
from email import policy
import pdfplumber
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load configuration from a JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

openai.api_key = config["openai_api_key"]
EMAIL_HOST = config["email_host"]
EMAIL_USER = config["email_user"]
EMAIL_PASS = config["email_pass"]

# Function to fetch the latest email
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

# Function to extract text from email and attachments
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

# Step 1: LLM Classification Prompt
def classify_email(total_text):
    classification_prompt = config["classification_prompt"].format(email_content=total_text)
    model = config.get("openai_model", "gpt-4-turbo")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an AI that classifies loan servicing emails."},
                  {"role": "user", "content": classification_prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Step 2: Key Data Extraction Prompt
def extract_data(total_text):
    extraction_prompt = config["extraction_prompt"].format(email_content=total_text)
    model = config.get("openai_model", "gpt-4-turbo")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an AI that extracts structured data from loan servicing emails."},
                  {"role": "user", "content": extraction_prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Step 3: Routing Logic
def route_request(classification_result):
    classification = eval(classification_result)
    request_type = classification.get("Request Type", "Unknown")
    routing_map = config["routing_map"]
    return routing_map.get(request_type, "General Queue")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_email', methods=['POST'])
def process_email():
    email_msg = fetch_latest_email()
    email_text, attachment_text = extract_email_content(email_msg)
    total_text = email_text + "\n" + attachment_text
    
    classification_result = classify_email(total_text)
    extraction_result = extract_data(total_text)
    assigned_team = route_request(classification_result)
    
    return jsonify({
        "classification_result": classification_result,
        "extraction_result": extraction_result,
        "assigned_team": assigned_team
    })

if __name__ == '__main__':
    app.run(debug=True)
