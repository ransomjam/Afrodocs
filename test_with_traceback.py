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
documents = [f for f in os.listdir(SAMPLES_DIR) if f.endswith('.docx')][:12]

print(f"Testing {len(documents)} documents with full traceback...")
print("=" * 80)

failed_count = 0
for idx, doc_name in enumerate(documents):
    print(f"\n[{idx+1}/{len(documents)}] Testing: {doc_name}...", end=" ")
    sys.stdout.flush()
    
    # Create a unique test user for each document
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    test_username = f"testuser{random_suffix}"
    test_email = f"test_{random_suffix}@example.com"
    test_password = f"TestPass{random_suffix}123"
    
    test_user_data = {
        "username": test_username,
        "email": test_email,
        "password": test_password
    }
    
    # Signup
    try:
        signup_response = requests.post(f"{BASE_URL}/api/auth/signup", json=test_user_data)
        if signup_response.status_code == 400:
            signup_msg = signup_response.json()
            if "already exists" in str(signup_msg):
                # User already exists, just login
                pass
            else:
                print(f"FAILED (signup error: {signup_response.status_code} - {signup_msg})")
                continue
        elif signup_response.status_code not in [200, 201]:
            print(f"FAILED (signup error: {signup_response.status_code})")
            print(f"   Response: {signup_response.text}")
            continue
    except Exception as e:
        print(f"FAILED (signup exception: {e})")
        continue
    
    # Login
    try:
        login_response = requests.post(f"{BASE_URL}/api/auth/login", json=test_user_data)
        if login_response.status_code != 200:
            print(f"FAILED (login error: {login_response.status_code})")
            print(f"   Response: {login_response.text}")
            continue
        
        auth_data = login_response.json()
        auth_token = auth_data.get('access_token') or auth_data.get('token')
        if not auth_token:
            print(f"FAILED (no token in login response)")
            print(f"   Response: {auth_data}")
            continue
    except Exception as e:
        print(f"FAILED (login exception: {e})")
        continue
    
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    # Upload document
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
            
            response = requests.post(f"{BASE_URL}/upload", files=files, data=data, headers=headers)
        
        if response.status_code == 200:
            print("PASSED")
        else:
            print(f"FAILED (status {response.status_code})")
            try:
                error_data = response.json()
                error_msg = error_data.get('error', 'Unknown error')
                print(f"   Error: {error_msg}")
                
                if 'traceback' in error_data:
                    print(f"\n   Full Traceback:")
                    for line in error_data['traceback'].split('\n'):
                        print(f"   {line}")
            except:
                print(f"   Response: {response.text}")
            
            failed_count += 1
    except Exception as e:
        print(f"FAILED (upload exception: {e})")
        traceback.print_exc()
        failed_count += 1

print("\n" + "=" * 80)
print(f"Results: {len(documents) - failed_count}/{len(documents)} passed, {failed_count} failed")
