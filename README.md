# 🚀 Email Classification and Data Extraction

## 📌 Table of Contents
- [Introduction](#-introduction)
- [Demo](#-demo)
- [Inspiration](#-inspiration)
- [What It Does](#%EF%B8%8F-what-it-does)
- [How We Built It](#%EF%B8%8F-how-we-built-it)
- [Challenges We Faced](#-challenges-we-faced)
- [How to Run](#-how-to-run)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Team](#-team)

---

## 🎯 Introduction
Loan servicing teams manually process high-volume emails which are diverse requests and attachments. Manual triage is time-consuming and error-prone,
Need an AI-powered solution to automate classification & data extraction.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:
![Image20250326133404](https://github.com/user-attachments/assets/773174b7-d4a3-4385-a2c4-06900ad51814)
![Image20250326133411](https://github.com/user-attachments/assets/8858414a-d4a0-43ee-8cad-b3110d749aab)

## 💡 Inspiration
Every day, banks and financial institutions handle an overwhelming volume of emails, each containing critical information for loan processing, compliance, risk assessment, and customer service. Manually sorting, classifying, and extracting key data from these emails is slow, error-prone, and inefficient.

Enter Generative AI (GenAI)—a revolutionary technology that can intelligently classify, extract, and route emails in real time. With advances in natural language processing (NLP) and deep learning, we can build a system that:

✅ Understands context – Unlike traditional rule-based systems, a GenAI-powered model comprehends the nuances of language, ensuring accurate classification.

✅ Extracts key data – Automatically identifies borrower details, loan amounts, contract terms, and action items.

✅ Routes emails intelligently – Directs emails to the right department, whether it’s underwriting, risk, or customer service, reducing delays and human intervention.

✅ Learns and improves – Continuously refines its accuracy through reinforcement learning, adapting to evolving business needs.

By integrating GenAI into commercial lending workflows, banks can speed up decision-making, reduce costs, and enhance customer satisfaction. This is the future of intelligent automation—turning email chaos into structured, actionable insights.

## ⚙️ What It Does
Features

### Email Fetching
Email fetching is the process of connecting to an Internet Message Access Protocol (IMAP) server to retrieve the latest emails from a user's inbox. This involves establishing a secure connection to the server, authenticating the user’s credentials, and then querying the server for any new messages since the last fetch. The system efficiently downloads the most recent emails, allowing for timely processing and ensuring that users have access to the latest communications. This step is crucial for maintaining an up-to-date workflow and is typically performed at regular intervals or triggered by specific user actions.

### Email Classification
Email classification is a sophisticated process that utilizes a Large Language Model (LLM) to analyze the content of incoming emails in order to accurately determine their request type and sub-type. This involves parsing the text of the email, including subject lines and body content, to identify keywords, phrases, and context that signify the nature of the request. For example, the LLM may classify an email as a "support request," "billing inquiry," or "general query," and further categorize it into sub-types such as "technical issue" or "payment problem." This systematic classification is vital for routing requests to the correct teams and ensuring a prompt response.

### Data Extraction
Data extraction is the process of identifying and pulling out key details from the email content and any attached files. This may include extracting information such as names, dates, order numbers, and specific details relevant to the request. Advanced algorithms may also be employed to scan attachments—like PDFs or images—to extract text or data using Optical Character Recognition (OCR) technology. The extracted information is then structured and formatted for easy use in subsequent processes, such as logging requests or generating reports, which enhances overall efficiency and accuracy in handling inquiries.

### Multi-Request Handling
Multi-request handling refers to the system's capability to recognize and manage emails containing multiple requests from a single sender. This involves analyzing the content to identify both primary and secondary requests, allowing the system to address each issue appropriately. For instance, an email may contain a request for assistance with a product issue while also asking about shipping status. By effectively categorizing and prioritizing these requests, the system ensures that all issues are acknowledged and resolved without neglecting any, thereby improving customer satisfaction and operational effectiveness.

### Duplicate Email Detection
Duplicate email detection is a critical feature that helps prevent redundant service requests by identifying emails that are identical or nearly identical in content. The system employs algorithms to compare incoming emails against a database of previously processed requests. If a duplicate is detected, the system can flag it, consolidate the request, or inform the user that their inquiry has already been received. This not only streamlines the workflow by reducing unnecessary duplication of efforts but also enhances resource allocation and response times.

### Skill-Based Routing
Skill-based routing is an intelligent system feature that assigns incoming requests to the appropriate team or personnel based on the classification results. Once the email has been classified, the system evaluates the specific skills and expertise of available personnel to determine the best fit for addressing the request. This ensures that inquiries are handled by individuals who have the relevant experience and knowledge, leading to quicker resolutions and a more efficient handling of cases. By directing requests to the most qualified teams, organizations can improve service quality and customer satisfaction.

### Web-Based UI
The web-based user interface (UI) provides a simple and intuitive frontend that allows users to view and interact with the results of the email processing system. This interface displays the classified requests, extracted data, and any relevant metrics in a clear and organized manner. Users can easily navigate through their emails, view detailed information about each request, and track the status of responses. The UI is designed for ease of use, enabling both technical and non-technical users to efficiently manage their email requests and access insights without needing extensive training or technical knowledge. Additionally, the web-based nature of the UI ensures accessibility from any device with internet connectivity, promoting flexibility and convenience in communication management.

## 🛠️ How We Built It
https://prezi.com/view/4r84XkOssKOz1MqGl56W/

## 🚧 Challenges We Faced

**OpenAI API quota exceeded**  
When we encounter an error indicating that the OpenAI API quota has been exceeded, it is essential to implement an effective strategy to manage our requests and ensure uninterrupted service. To address this issue, we can integrate **retry logic** into our application. This involves setting up a mechanism that will automatically attempt to resend the request after a specified interval when it detects that the quota has been reached. By incorporating exponential backoff algorithms, we can gradually increase the waiting time between retries, which helps to minimize the number of requests sent during peak load times. Additionally, we can explore the option of **switching models**. If we have access to multiple models through the OpenAI API, we can dynamically select a different model that may have a different quota or usage limits, thereby allowing our application to continue functioning while complying with the API restrictions.

---

**IMAP authentication error**  
In the event of an IMAP authentication error, it is crucial to ensure that our application can securely access the email accounts it needs to manage. To resolve this issue, we have opted to use **App Passwords**. App Passwords are a form of two-factor authentication that generates a unique password specifically for applications that do not support modern authentication protocols. By enabling App Passwords in the email account settings, we can provide a more secure method for our application to authenticate with the IMAP server. This not only enhances security by avoiding the use of the primary account password but also allows us to comply with best practices in user authentication.

---

**Template Not Found**  
When faced with a "Template Not Found" error in our Flask application, it is vital to ensure that our project is correctly configured to locate and serve the necessary HTML templates. To address this issue, we have taken steps to **ensure correct Flask template paths**. To address this issue, we have taken several proactive steps to ensure that the Flask template paths are correctly configured and functioning as intended. This includes a comprehensive review of our project structure to verify that all template files are located in their designated directories. We have also implemented a systematic approach to managing the template loading process, ensuring that the Flask application can accurately locate and render the necessary HTML files.

Additionally, we have updated our configuration settings to explicitly define the paths for our template folders, avoiding any ambiguity that could lead to errors. We are employing Flask’s built-in functionalities, such as the `template_folder` parameter, to specify the location of our templates clearly.

Furthermore, we have enhanced our development workflow by integrating testing procedures that validate the accessibility of each template before deployment. This includes writing unit tests that check for the existence of templates and confirm that they render correctly without errors when called from the application.

By implementing these measures, we aim to eliminate any potential issues related to incorrect template paths, thereby improving the stability and reliability of our Flask application. Our commitment to maintaining an organized and well-structured template system will ultimately enhance the overall user experience and streamline the development process.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-xtreme-thinkers.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
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
   ```




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

## 🏗️ Tech Stack


**Python (Flask for Web UI, IMAP for Email Fetching)**  
We utilize Python as the primary programming language due to its versatility and robust ecosystem. Within this framework, we leverage Flask, a lightweight web framework, to create an intuitive and responsive web user interface (UI). Flask allows us to easily set up routes, handle user input, and render dynamic HTML content, making it straightforward for users to interact with our application. To facilitate the retrieval of emails, we implement the Internet Message Access Protocol (IMAP). This allows our application to securely connect to email servers, fetch relevant messages, and manage email folders efficiently. With IMAP, we can seamlessly access and process incoming emails, ensuring that users receive timely updates and notifications.

**OpenAI GPT (Email Classification & Data Extraction)**  
To enhance our application's functionality, we incorporate OpenAI's Generative Pre-trained Transformer (GPT) models. These advanced AI algorithms are designed for natural language processing, making them ideal for classifying incoming emails based on their content and intent. By utilizing GPT, we can automatically categorize emails into predefined classes such as inquiries, complaints, or requests, streamlining the workflow for users. Additionally, GPT aids in data extraction, allowing us to pull relevant information from the body of the email or attachments, such as names, dates, and specific queries. This capability not only improves response accuracy but also reduces the manual effort required to sort and respond to emails.

**PDFplumber (OCR for Extracting Text from Attachments)**  
To handle attachments, particularly those in PDF format, we employ PDFplumber, a powerful library designed for extracting text from PDF documents. Many emails may contain important attachments that require analysis, and PDFplumber allows us to perform Optical Character Recognition (OCR) on scanned documents. This means we can convert images of text in PDFs into machine-readable text, enabling us to extract valuable information that can be further processed. By integrating PDFplumber into our workflow, we ensure that no critical data is overlooked, regardless of the format in which it is presented.

**JSON-Based Configurable Rules**  
Our application is designed with flexibility in mind, utilizing JSON (JavaScript Object Notation) as a means to implement configurable rules. This allows users to define and adjust criteria for email classification and data extraction without needing to modify the underlying codebase. By storing rules in a JSON format, users can easily update parameters such as keywords, categories, and extraction guidelines. This configuration method not only enhances usability but also empowers users to customize the application to meet their specific needs and workflows, adapting to changing requirements over time.

**GitHub for Version
## 👥 Team
- **Harihara Pamidi** - [GitHub](#) | [LinkedIn](#)
- **Pavan Kumar Harikeerthi** - [GitHub](#) | [LinkedIn](#)
- **Shiva Papini** - [GitHub](#) | [LinkedIn](#)
- **Rupesh Pachipala** - [GitHub](#) | [LinkedIn](#)
