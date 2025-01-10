# Zaptasks

Python automation to notify you on WhatsApp about your Google Calendar's today's events

# Requirements

- Python 3 or later;
- Access to Google Calender API. Access the [Google Calendar API Guide](https://developers.google.com/calendar/api/quickstart/python?hl=pt-br) to enable the API.

# Environment file

- Make a copy of .env.example and save it as .env;
- Fill the CONTACT_NUMBER variable with the number you want to send the events to.

# Installation

```bash
# Clone the repository
git clone repo_url

# Create the python virtual environment
python3 -m venv venv

# Enable virtual environment
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

# Commands

```bash
# Log in to WhatsApp Web
python login.py

# Send Google Calendar's today's events to WhatsApp
python main.py
```

# Author

João Faust