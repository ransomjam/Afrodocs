#!/usr/bin/env python
import requests
import json
import os
import random
import string
import traceback
import sys

# Force UTF-8 output
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = "http://localhost:5000"

# Sample documents
SAMPLES_DIR = "Samples"
documents = sorted([f for f in os.listdir(SAMPLES_DIR) if f.endswith('.docx')])[:12]

print(f"Testing {len(documents)} documents...")
print("=" * 80)

failed_docs = []
passed_docs = []

for idx, doc_name in enumerate(documents):
    print(f"[{idx+1}/{len(documents)}] {doc_name}...", end=" ", flush=True)
    
    # Create a unique test user for this document
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
    try:
        signup_response = session.post(f"{BASE_URL}/api/auth/signup", json=test_user_data)
        if signup_response.status_code not in [200, 201]:
            print(f"FAILED (signup error: {signup_response.status_code})")
            print(f"  Response: {signup_response.text}")
            failed_docs.append((doc_name, f"signup error {signup_response.status_code}"))
            continue
    except Exception as e:
        print(f"FAILED (signup exception: {str(e)[:100]})")
        failed_docs.append((doc_name, f"signup exception: {str(e)[:50]}"))
        continue
    
    # Login
    try:
        login_response = session.post(f"{BASE_URL}/api/auth/login", json=test_user_data)
        if login_response.status_code != 200:
            print(f"FAILED (login error)")
            failed_docs.append((doc_name, "login failed"))
            continue
    except Exception as e:
        print(f"FAILED (login exception)")
        failed_docs.append((doc_name, "login exception"))
        continue
    
    # Upload document with session (cookies will be sent automatically)
    doc_path = os.path.join(SAMPLES_DIR, doc_name)
    try:
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
        
        if response.status_code == 200:
            print("PASSED")
            passed_docs.append(doc_name)
        else:
            print(f"FAILED ({response.status_code})")
            try:
                error_data = response.json()
                error_msg = error_data.get('error', 'Unknown error')
                print(f"   Error: {error_msg}")
                
                if 'traceback' in error_data:
                    print(f"\n   TRACEBACK:")
                    print("   " + "\n   ".join(error_data['traceback'].split('\n')))
                else:
                    print(f"   Response: {response.text[:500]}")
            except:
                print(f"   Response: {response.text[:200]}")
            
            failed_docs.append((doc_name, error_data.get('error', 'Unknown error')))
    except Exception as e:
        print(f"FAILED (upload exception)")
        failed_docs.append((doc_name, f"upload exception: {str(e)}"))

print("\n" + "=" * 80)
print(f"Results: {len(passed_docs)}/{len(documents)} passed\n")

if failed_docs:
    print(f"FAILED DOCUMENTS ({len(failed_docs)}):")
    for doc, reason in failed_docs:
        print(f"  - {doc}: {reason}")
