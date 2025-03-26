@echo off
echo Setting up the GenAI Email POC...

:: Move to the script directory
cd /d %~dp0

:: Install dependencies
pip install -r requirements.txt

:: Run the application
python -m app.main
