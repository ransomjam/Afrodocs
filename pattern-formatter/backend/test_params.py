#!/usr/bin/env python3
"""
Test to verify formatting parameters are actually being sent from frontend
"""

import requests
import json
from pathlib import Path

# Create a test file
test_file = "test_doc.txt"
with open(test_file, 'w') as f:
    f.write("Test document\n" * 100)

# Prepare parameters
params = {
    'include_toc': 'true',
    'font_size': '14',
    'line_spacing': '1.5', 
    'margin_cm': '2.0'
}

print("📤 Testing parameter send:")
print(f"   include_toc: {params['include_toc']} (type: {type(params['include_toc'])})")
print(f"   font_size: {params['font_size']} (type: {type(params['font_size'])})")
print(f"   line_spacing: {params['line_spacing']} (type: {type(params['line_spacing'])})")
print(f"   margin_cm: {params['margin_cm']} (type: {type(params['margin_cm'])})")

# Login
session = requests.Session()
login_url = "http://localhost:5000/api/auth/login"
login_data = {'username': 'admin', 'password': 'admin123'}

login_response = session.post(login_url, json=login_data)
print(f"\n✓ Login: {login_response.status_code}")

# Upload with parameters
with open(test_file, 'rb') as f:
    files = {'file': f}
    upload_url = "http://localhost:5000/upload"
    
    response = session.post(upload_url, files=files, data=params)
    print(f"\n✓ Upload response: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        job_id = result['job_id']
        print(f"   Job ID: {job_id}")
        
        # Give it a moment to complete
        import time
        time.sleep(1)
        
        # Check the metadata file to see what was recorded
        meta_file = Path(f"./outputs/{job_id}_meta.json")
        if meta_file.exists():
            with open(meta_file, 'r') as mf:
                metadata = json.load(mf)
                print(f"\n📋 Metadata recorded:")
                print(json.dumps(metadata, indent=2))
        
        # Now check the document
        from docx import Document
        doc_file = Path(f"./outputs/{job_id}_formatted.docx")
        if doc_file.exists():
            doc = Document(str(doc_file))
            print(f"\n📋 Document properties:")
            
            if doc.sections:
                section = doc.sections[0]
                margin_inches = section.top_margin.inches
                margin_cm_actual = margin_inches * 2.54
                print(f"   Margin: {margin_cm_actual:.2f} cm (requested: 2.0 cm)")
            
            # Check font size in Normal style
            try:
                normal = doc.styles['Normal']
                if normal.font.size:
                    font_pt = normal.font.size.pt
                    print(f"   Font size (Normal style): {font_pt} pt (requested: 14 pt)")
                if normal.paragraph_format.line_spacing:
                    print(f"   Line spacing (Normal style): {normal.paragraph_format.line_spacing}")
            except:
                pass
    else:
        print(f"   Error: {response.json()}")

# Clean up
import os
if os.path.exists(test_file):
    os.remove(test_file)
