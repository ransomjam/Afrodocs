#!/usr/bin/env python3
"""
Simple test to debug formatting options
"""

import requests
import json
from pathlib import Path

# Create test file
test_file = "test_doc.txt"
with open(test_file, 'w') as f:
    f.write("Test document\n" * 100)

params = {
    'include_toc': 'true',
    'font_size': '14',
    'line_spacing': '1.5', 
    'margin_cm': '2.0'
}

# Login
session = requests.Session()
login_url = "http://localhost:5000/api/auth/login"
login_data = {'username': 'admin', 'password': 'admin123'}

login_response = session.post(login_url, json=login_data)
print(f"Login: {login_response.status_code}")

# Upload
with open(test_file, 'rb') as f:
    files = {'file': f}
    upload_url = "http://localhost:5000/upload"
    response = session.post(upload_url, files=files, data=params)
    print(f"Upload: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        job_id = result['job_id']
        print(f"Job ID: {job_id}")
        print(f"Sent params: font_size=14, line_spacing=1.5, margin_cm=2.0, include_toc=true")
        
        import time
        time.sleep(2)
        
        # Check document
        from docx import Document
        doc_file = Path(f"./outputs/{job_id}_formatted.docx")
        if doc_file.exists():
            doc = Document(str(doc_file))
            print(f"\nDocument properties:")
            
            if doc.sections:
                margin_cm_actual = doc.sections[0].top_margin.inches * 2.54
                print(f"  Margin: {margin_cm_actual:.2f} cm (expected 2.0)")
            
            try:
                normal = doc.styles['Normal']
                if normal.font.size:
                    print(f"  Font size: {normal.font.size.pt} pt (expected 14)")
                if normal.paragraph_format.line_spacing:
                    print(f"  Line spacing: {normal.paragraph_format.line_spacing} (expected 1.5)")
            except:
                pass

import os
if os.path.exists(test_file):
    os.remove(test_file)
