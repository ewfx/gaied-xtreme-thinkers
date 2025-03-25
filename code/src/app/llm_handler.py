import openai
import json

# Load configuration
with open("app/config.json", "r") as config_file:
    config = json.load(config_file)

from openai import OpenAI

client = OpenAI(api_key=config["openai_api_key"])

def classify_email(total_text):
    classification_prompt = config["classification_prompt"].format(email_content=total_text)
    model = config.get("openai_model", "gpt-4-turbo")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an AI that classifies loan servicing emails."},
                  {"role": "user", "content": classification_prompt}]
    )
    return response["choices"][0]["message"]["content"]

def extract_data(total_text):
    extraction_prompt = config["extraction_prompt"].format(email_content=total_text)
    model = config.get("openai_model", "gpt-4-turbo")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an AI that extracts structured data from loan servicing emails."},
                  {"role": "user", "content": extraction_prompt}]
    )
    return response["choices"][0]["message"]["content"]

def route_request(classification_result):
    classification = eval(classification_result)
    request_type = classification.get("Request Type", "Unknown")
    routing_map = config["routing_map"]
    return routing_map.get(request_type, "General Queue")
