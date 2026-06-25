import requests
import os
from dotenv import load_dotenv

load_dotenv()

FORM_URL = os.getenv("FORM_URL")

def submit_to_google_form(name, phone, email, status, course):
    """Submit registration data to Google Form."""

    payload = {
        "entry.711707292":  name,
        "entry.1634097018": phone,
        "entry.1037507495": email,
        "entry.256001454":  status,
        "entry.2072888748": course
    }

    try:
        response = requests.post(FORM_URL, data=payload, timeout=10)
        return response.status_code  # 200 = success
    except Exception as e:
        print(f"Google Form Error: {e}")
        return 0  # Return 0 on failure so app.py handles it gracefully