from flask import Flask, render_template, request, jsonify
from app.email_processor import fetch_latest_email, extract_email_content
from app.llm_handler import classify_email, extract_data, route_request

app = Flask(__name__)

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
