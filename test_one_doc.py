#!/usr/bin/env python
import requests
import json
import os
import random
import string

BASE_URL = "http://localhost:5000"
SAMPLES_DIR = "Samples"

# Test just one failing document
doc_name = "Sample with Certification.docx"

random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
test_username = f"testuser{random_suffix}"
test_email = f"test_{random_suffix}@example.com"
test_password = f"TestPass{random_suffix}123"

test_user_data = {
    "username": test_username,
    "email": test_email,
    "password": test_password
}

session = requests.Session()

# Signup
signup_response = session.post(f"{BASE_URL}/api/auth/signup", json=test_user_data)
print(f"Signup: {signup_response.status_code}")

# Login
login_response = session.post(f"{BASE_URL}/api/auth/login", json=test_user_data)
print(f"Login: {login_response.status_code}")

# Upload document
doc_path = os.path.join(SAMPLES_DIR, doc_name)
with open(doc_path, 'rb') as f:
    files = {'file': (doc_name, f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
    data = {
        'font_size': '11',
        'line_spacing': '1.5',
        'margin_left': '1',
        'margin_top': '1',
        'margin_bottom': '1',
        'margin_right': '1',
        'formatting_options': json.dumps({
            'apply_formatting': True,
            'add_page_numbers': True,
            'add_headers': True,
            'add_footers': True
        })
    }
    
    response = session.post(f"{BASE_URL}/upload", files=files, data=data)

print(f"\nUpload Response: {response.status_code}")
error_data = response.json()

if 'traceback' in error_data:
    print("\nFull Traceback:")
    print(error_data['traceback'])
else:
    print("\nError Response:")
    print(json.dumps(error_data, indent=2))
