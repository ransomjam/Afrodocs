#!/usr/bin/env python3
"""
Test to trigger and capture the "name 'i' is not defined" error
"""

import requests
import os
import json

API_BASE = "http://localhost:5000"
SAMPLES_FOLDER = r"c:\Users\user\Desktop\PATTERN\Samples"

def test_upload_with_error_capture():
    print("Creating test user...")
    username = f"errortest_{os.urandom(2).hex()}"
    password = "test123"
    
    # Create user
    sig = requests.post(f"{API_BASE}/api/auth/signup", 
                        json={"username": username, "password": password})
    print(f"Signup: {sig.status_code}")
    
    # Login
    login = requests.post(f"{API_BASE}/api/auth/login", 
                          json={"username": username, "password": password})
    cookies = login.cookies
    print(f"Login: {login.status_code}")
    
    # Try uploading a document that causes the error
    test_files = [
        "sample project with tables.docx",  # This one triggered the error
        "Jam _ sample project with figures.docx"
    ]
    
    for doc_file in test_files:
        doc_path = os.path.join(SAMPLES_FOLDER, doc_file)
        if not os.path.exists(doc_path):
            print(f"SKIP: {doc_file} not found")
            continue
        
        print(f"\nTesting upload: {doc_file}")
        print("=" * 70)
        
        with open(doc_path, 'rb') as f:
            files = {'file': (doc_file, f)}
            data = {
                'include_toc': 'false',
                'font_size': '12',
                'line_spacing': '1.5',
                'margin_cm': '2.5'  # Try with uniform margin
            }
            
            resp = requests.post(
                f"{API_BASE}/upload",
                files=files,
                data=data,
                cookies=cookies,
                timeout=120
            )
            
            print(f"Response Status: {resp.status_code}")
            
            try:
                result = resp.json()
                print(f"Response JSON: {json.dumps(result, indent=2)}")
                
                if 'error' in result:
                    print(f"\n✗ ERROR CAPTURED:")
                    print(f"  Message: {result['error']}")
                    
                    if "name 'i' is not defined" in str(result['error']):
                        print("\n🔍 FOUND THE ERROR: name 'i' is not defined")
                        print("This error needs to be fixed in the backend!")
            except Exception as e:
                print(f"Response text: {resp.text}")
                print(f"Parsing error: {str(e)}")

if __name__ == "__main__":
    test_upload_with_error_capture()
