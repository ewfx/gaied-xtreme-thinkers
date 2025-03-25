GenAI Email Classification & Data Extraction POC

Overview

This project is a Proof of Concept (POC) for automating email classification and data extraction using Generative AI (LLMs). It processes emails received by Commercial Bank Lending Service teams, classifies requests, extracts key details, and routes service requests efficiently.

Features

Email Fetching: Retrieves the latest email from an IMAP server.

Email Classification: Uses an LLM to determine the request type and sub-type.

Data Extraction: Extracts key details from email content and attachments.

Multi-Request Handling: Identifies primary and secondary requests.

Duplicate Email Detection: Prevents redundant service requests.

Skill-Based Routing: Assigns requests to the appropriate team based on classification.

Web-Based UI: A simple frontend for viewing results.

Installation & Setup

Prerequisites

Python 3.8+

OpenAI API Key

IMAP Email Access

Flask for the web UI

Installation

Clone the repository:

git clone https://github.com/your-repo/genai-email-poc.git
cd genai-email-poc

Install dependencies:

pip install -r requirements.txt

Configure the config.json file with your OpenAI API key and email credentials:

{
    "openai_api_key": "your-api-key",
    "email_host": "imap.example.com",
    "email_user": "your-email@example.com",
    "email_pass": "your-password",
    "openai_model": "gpt-4",
    "classification_prompt": "Classify the following email: {email_content}",
    "extraction_prompt": "Extract structured data from this email: {email_content}",
    "routing_map": { "Loan Adjustment": "Loan Processing Team" }
}

Running the Application

Option 1: Run with Shell Script (Linux/macOS)

chmod +x run.sh
./run.sh

Option 2: Run with Batch Script (Windows)

run.bat

Option 3: Manually Start Flask App

python app.py

Once running, access the UI at http://127.0.0.1:5000/.

Running Unit Tests

Navigate to the unit_tests directory:

cd unit_tests

Run all tests:

python -m unittest discover

Folder Structure

├── app.py               # Main application file
├── config.json          # Configuration file
├── templates/           # HTML files for web UI
│   ├── index.html
├── static/              # Static files (CSS, JS)
├── unit_tests/          # Unit test scripts
│   ├── test_email_fetch.py
│   ├── test_classification.py
│   ├── test_data_extraction.py
│   ├── test_routing.py
├── requirements.txt     # Python dependencies
├── run.sh               # Shell script to start app
├── run.bat              # Windows batch script to start app
├── README.md            # Project documentation

Future Enhancements

Integration with enterprise email systems (e.g., Outlook, Gmail API)

Improved LLM fine-tuning for domain-specific requests

Enhanced UI for monitoring email processing status

License

This project is open-source and available under the MIT License.
