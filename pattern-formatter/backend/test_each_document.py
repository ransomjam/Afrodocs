#!/usr/bin/env python3
"""
Test each document individually to identify which one causes the error
"""

import requests
import os

API_BASE = "http://localhost:5000"
SAMPLES_FOLDER = r"c:\Users\user\Desktop\PATTERN\Samples"

def test_single_document(doc_path):
    """Test a single document and return detailed error if any"""
    doc_name = os.path.basename(doc_path)
    
    # Create fresh user
    username = f"test_{os.urandom(2).hex()}"
    password = "test123"
    
    sig = requests.post(f"{API_BASE}/api/auth/signup", 
                        json={"username": username, "password": password})
    
    login = requests.post(f"{API_BASE}/api/auth/login", 
                          json={"username": username, "password": password})
    cookies = login.cookies
    
    # Upload
    with open(doc_path, 'rb') as f:
        files = {'file': (doc_name, f)}
        data = {'include_toc': 'false', 'margin_cm': '2.5'}
        
        resp = requests.post(
            f"{API_BASE}/upload",
            files=files,
            data=data,
            cookies=cookies,
            timeout=120
        )
        
        return resp.status_code, resp.json()

print("Testing each document individually...\n")

for doc in sorted(os.listdir(SAMPLES_FOLDER)):
    if not doc.endswith('.docx') or doc.startswith('~'):
        continue
    
    doc_path = os.path.join(SAMPLES_FOLDER, doc)
    print(f"Testing: {doc}...", end=" ")
    
    try:
        status, result = test_single_document(doc_path)
        
        if status == 200:
            print("✓ SUCCESS")
        else:
            error = result.get('error', 'Unknown error')
            print(f"✗ FAILED")
            print(f"  Error: {error}")
            if "name 'i' is not defined" in error:
                print(f"  👉 THIS DOCUMENT CAUSES THE ERROR")
    except Exception as e:
        print(f"✗ EXCEPTION: {str(e)}")

print("\nDone!")
