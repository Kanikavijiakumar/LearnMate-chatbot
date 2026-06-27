import requests
import os
from dotenv import load_dotenv

load_dotenv()

FORM_URL = os.getenv("FORM_URL")

def submit_to_google_form(name, phone, email, status, course):
    payload = {
        "entry.711707292": name,
        "entry.1634097018": phone,
        "entry.1037507495": email,
        "entry.256001454": status,
        "entry.2072888748": course
    }
    try:
        response = requests.post(FORM_URL, data=payload, timeout=10)
        return response.status_code
    except Exception as e:
        print(f"Error: {e}")
        return 0