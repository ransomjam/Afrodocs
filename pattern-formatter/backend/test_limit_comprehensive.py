#!/usr/bin/env python3
"""
More comprehensive test - uploads documents until reaching the 300-page limit.
"""

import requests
import os
from pathlib import Path

API_BASE = "http://localhost:5000"

# Sample documents to test with
SAMPLES_FOLDER = r"c:\Users\user\Desktop\PATTERN\Samples"
TEST_DOCUMENTS = [
    "sample project with tables.docx",
    "sample report with bullet points.docx",
    "sample_dissertation.docx",
    "Sample with Certification.docx",
    "sample with breaks.docx",
    "sample report with missing content issues.docx",
    "sample report with bullet points.docx",
    "sample project with tables.docx",
]

def main():
    print("\n" + "="*70)
    print("COMPREHENSIVE 300-PAGE LIMIT TEST")
    print("="*70)
    
    # Create test user
    print("\nStep 1: Create test user...")
    username = "limittest_2"
    password = "test123"
    
    sig_resp = requests.post(
        f"{API_BASE}/api/auth/signup",
        json={"username": username, "password": password}
    )
    print(f"Signup: {sig_resp.status_code}")
    
    # Login
    print("Step 2: Login...")
    login_resp = requests.post(
        f"{API_BASE}/api/auth/login",
        json={"username": username, "password": password}
    )
    print(f"Login: {login_resp.status_code}")
    
    if login_resp.status_code != 200:
        print("Login failed!")
        return
    
    cookies = login_resp.cookies
    
    # Check initial status
    status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
    print(f"\nInitial Status:")
    print(f"  Pages used: {status['pages_this_month']}/300")
    print(f"  Plan: {status['plan']}")
    
    # Upload documents
    print("\n" + "="*70)
    print("Step 3: Upload Documents")
    print("="*70)
    
    total_uploaded = 0
    limit_hit = False
    
    for idx, doc_name in enumerate(TEST_DOCUMENTS, 1):
        doc_path = os.path.join(SAMPLES_FOLDER, doc_name)
        
        if not os.path.exists(doc_path):
            print(f"\n[{idx}] SKIP: {doc_name} (not found)")
            continue
        
        # Check current status
        status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
        current = status['pages_this_month']
        remaining = 300 - current
        
        print(f"\n[{idx}] {doc_name}")
        print(f"    Current: {current}/300 pages ({remaining} remaining)")
        
        if remaining <= 0:
            print(f"    STOP: Quota exhausted!")
            break
        
        # Upload
        try:
            with open(doc_path, 'rb') as f:
                files = {'file': (doc_name, f)}
                data = {
                    'include_toc': 'false',
                    'font_size': '12',
                    'line_spacing': '1.5',
                    'margin_cm': '2.5'
                }
                
                resp = requests.post(
                    f"{API_BASE}/upload",
                    files=files,
                    data=data,
                    cookies=cookies,
                    timeout=60
                )
                
                if resp.status_code == 200:
                    result = resp.json()
                    pages = result.get('pages', 0)
                    print(f"    ✓ Success: {pages} pages")
                    total_uploaded += 1
                else:
                    result = resp.json()
                    if result.get('error') == 'LIMIT_REACHED':
                        print(f"    ✗ LIMIT REACHED!")
                        print(f"      Message: {result.get('message')}")
                        print(f"      Required: {result.get('required')} pages")
                        limit_hit = True
                        break
                    else:
                        print(f"    ✗ Error: {result.get('error')}")
        except Exception as e:
            print(f"    ✗ Exception: {str(e)}")
    
    # Final status
    print("\n" + "="*70)
    print("FINAL RESULTS")
    print("="*70)
    
    status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
    final_pages = status['pages_this_month']
    
    print(f"\nDocuments uploaded: {total_uploaded}")
    print(f"Final pages used: {final_pages}/300")
    print(f"Limit enforcement: {'✓ WORKING' if limit_hit or final_pages >= 300 else '⚠ NOT REACHED'}")
    
    if limit_hit:
        print(f"\n✓✓✓ LIMIT TEST PASSED ✓✓✓")
        print(f"    System correctly enforced the 300-page limit!")
    elif final_pages >= 300:
        print(f"\n✓✓✓ LIMIT TEST PASSED ✓✓✓")
        print(f"    Reached exactly 300 pages as expected!")
    else:
        print(f"\n⚠ Test incomplete - reached {final_pages} pages")
        remaining = 300 - final_pages
        print(f"    Need {remaining} more pages to reach limit")

if __name__ == "__main__":
    main()
