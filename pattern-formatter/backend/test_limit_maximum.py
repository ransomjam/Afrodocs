#!/usr/bin/env python3
"""
Test to push as close as possible to the 300-page limit
"""

import requests
import os

API_BASE = "http://localhost:5000"
SAMPLES_FOLDER = r"c:\Users\user\Desktop\PATTERN\Samples"

# Get all available documents
available_docs = [
    f for f in os.listdir(SAMPLES_FOLDER) 
    if f.endswith('.docx') and not f.startswith('~')
]

def main():
    print("\n" + "="*70)
    print("300-PAGE LIMIT - PUSH TO MAXIMUM TEST")
    print("="*70)
    
    # Create new user
    print("\nCreating new test user...")
    username = f"maxtest_{int(os.urandom(2).hex(), 16)}"
    password = "test123"
    
    sig = requests.post(f"{API_BASE}/api/auth/signup", 
                        json={"username": username, "password": password})
    print(f"User created: {username}")
    
    # Login
    login = requests.post(f"{API_BASE}/api/auth/login", 
                          json={"username": username, "password": password})
    cookies = login.cookies
    
    # Show initial status
    status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
    print(f"Starting: {status['pages_this_month']}/300 pages")
    
    # Upload documents repeatedly
    print("\n" + "="*70)
    print("Uploading documents to reach limit...")
    print("="*70)
    
    upload_count = 0
    
    for doc in available_docs[:20]:  # Try first 20 files
        doc_path = os.path.join(SAMPLES_FOLDER, doc)
        if not os.path.isfile(doc_path):
            continue
        
        status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
        current = status['pages_this_month']
        
        if current >= 300:
            print(f"\n✓ Reached 300 pages!")
            break
        
        remaining = 300 - current
        print(f"\n[{upload_count + 1}] {doc}")
        print(f"    Current: {current}/300 (need: {remaining})")
        
        try:
            with open(doc_path, 'rb') as f:
                resp = requests.post(
                    f"{API_BASE}/upload",
                    files={'file': (doc, f)},
                    data={'include_toc': 'false', 'margin_cm': '2.5'},
                    cookies=cookies,
                    timeout=60
                )
                
                if resp.status_code == 200:
                    upload_count += 1
                    print(f"    ✓ Uploaded")
                else:
                    result = resp.json()
                    if result.get('error') == 'LIMIT_REACHED':
                        print(f"    ✗ LIMIT BLOCKED!")
                        print(f"       Error: {result.get('message')}")
                        break
                    else:
                        print(f"    ✗ {result.get('error')}")
        except Exception as e:
            print(f"    ✗ {str(e)}")
    
    # Final report
    status = requests.get(f"{API_BASE}/api/auth/status", cookies=cookies).json()
    final = status['pages_this_month']
    
    print("\n" + "="*70)
    print("FINAL TEST REPORT")
    print("="*70)
    print(f"Documents uploaded: {upload_count}")
    print(f"Total pages: {final}/300")
    print(f"Percentage: {(final/300)*100:.1f}%")
    
    if final >= 300:
        print(f"\n✅ LIMIT TEST PASSED - Reached {final} pages!")
    elif final >= 270:
        print(f"\n✅ LIMIT TEST PASSED - Reached {final} pages (90% of limit)!")
    else:
        print(f"\n⚠ Reached {final} pages ({(final/300)*100:.1f}%)")

if __name__ == "__main__":
    main()
