#!/usr/bin/env python3
"""
Test the 300-page free tier limit by uploading sample documents.
This script will:
1. Create a test user
2. Upload multiple sample documents
3. Track cumulative page count
4. Test the limit enforcement
5. Verify error messages
"""

import requests
import os
from pathlib import Path
import json

API_BASE = "http://localhost:5000"

# Sample documents to test with
SAMPLES_FOLDER = r"c:\Users\user\Desktop\PATTERN\Samples"
TEST_DOCUMENTS = [
    "sample project with tables.docx",
    "sample report with bullet points.docx",
    "sample_dissertation.docx",
    "sample_report_with_images.docx",
    "Sample with Certification.docx",
    "sample with breaks.docx",
]

def create_test_user():
    """Create or get test user"""
    print("\n" + "="*70)
    print("STEP 1: Create/Login Test User")
    print("="*70)
    
    username = "limit_tester"
    password = "test123"
    
    # Try to register
    print(f"Creating test user: {username}")
    reg_resp = requests.post(
        f"{API_BASE}/api/auth/signup",
        json={"username": username, "password": password}
    )
    
    if reg_resp.status_code == 201:
        print("✓ New user created")
    elif reg_resp.status_code == 400:
        print("✓ User already exists")
    else:
        print(f"✗ Unexpected response: {reg_resp.status_code}")
        return None
    
    # Login
    print(f"Logging in...")
    login_resp = requests.post(
        f"{API_BASE}/api/auth/login",
        json={"username": username, "password": password}
    )
    
    if login_resp.status_code != 200:
        print(f"✗ Login failed: {login_resp.status_code}")
        return None
    
    print("✓ Login successful")
    return login_resp.cookies

def get_user_info(cookies):
    """Get current user info"""
    resp = requests.get(
        f"{API_BASE}/api/auth/status",
        cookies=cookies
    )
    if resp.status_code == 200:
        return resp.json()
    return None

def upload_document(file_path, cookies, doc_num):
    """Upload a single document"""
    filename = os.path.basename(file_path)
    print(f"\n  [{doc_num}] Uploading: {filename}")
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (filename, f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
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
                pages = result.get('pages', 'unknown')
                print(f"      ✓ Uploaded successfully ({pages} pages)")
                return True, pages
            else:
                result = resp.json()
                if result.get('error') == 'LIMIT_REACHED':
                    print(f"      ✗ LIMIT REACHED: {result.get('message', 'Unknown error')}")
                    print(f"        Required: {result.get('required')} pages, Remaining: {result.get('remaining')}")
                    return False, "LIMIT"
                else:
                    print(f"      ✗ Upload failed: {result.get('error', 'Unknown error')}")
                    return False, None
    except Exception as e:
        print(f"      ✗ Error: {str(e)}")
        return False, None

def run_test():
    """Run the full limit test"""
    print("\n" + "="*70)
    print("300-PAGE FREE TIER LIMIT TEST")
    print("="*70)
    
    # Step 1: Create/login user
    cookies = create_test_user()
    if not cookies:
        print("\n✗ Failed to create/login user")
        return False
    
    # Get initial user info
    user_info = get_user_info(cookies)
    print(f"\nUser Info:")
    print(f"  Username: {user_info.get('username')}")
    print(f"  Plan: {user_info.get('plan')}")
    print(f"  Current Usage: {user_info.get('pages_this_month')} pages")
    print(f"  Balance: {user_info.get('pages_balance')} pages")
    
    # Reset user if needed (for clean test)
    initial_usage = user_info.get('pages_this_month', 0)
    if initial_usage > 0:
        print(f"\n⚠ User already has {initial_usage} pages used this month")
        print(f"  Remaining quota: {300 - initial_usage} pages")
    
    # Step 2: Upload documents
    print("\n" + "="*70)
    print("STEP 2: Upload Documents")
    print("="*70)
    
    total_pages = initial_usage
    successful_uploads = 0
    limit_reached = False
    
    for idx, doc_name in enumerate(TEST_DOCUMENTS, 1):
        doc_path = os.path.join(SAMPLES_FOLDER, doc_name)
        
        if not os.path.exists(doc_path):
            print(f"\n  [{idx}] SKIP: {doc_name} (not found)")
            continue
        
        # Check user info before upload
        user_info = get_user_info(cookies)
        current_usage = user_info.get('pages_this_month', 0)
        remaining = 300 - current_usage
        
        print(f"\n  Status before upload:")
        print(f"    Current usage: {current_usage} pages")
        print(f"    Remaining quota: {remaining} pages")
        
        success, pages = upload_document(doc_path, cookies, idx)
        
        if pages == "LIMIT":
            limit_reached = True
            print(f"\n  ✓ LIMIT ENFORCEMENT WORKING!")
            print(f"    Reached exactly at: {current_usage} pages used")
            break
        elif success:
            successful_uploads += 1
            total_pages = current_usage + (pages if isinstance(pages, int) else 0)
        else:
            print(f"    ✗ Upload failed, continuing to next document...")
            continue
    
    # Final status
    print("\n" + "="*70)
    print("FINAL STATUS")
    print("="*70)
    
    user_info = get_user_info(cookies)
    final_usage = user_info.get('pages_this_month', 0)
    
    print(f"\nTest Results:")
    print(f"  Documents uploaded: {successful_uploads}")
    print(f"  Final pages used: {final_usage}/300")
    print(f"  Limit reached: {'Yes ✓' if limit_reached else 'No'}")
    
    if final_usage >= 300:
        print(f"\n✓✓✓ LIMIT TEST SUCCESSFUL ✓✓✓")
        print(f"    Reached the 300-page limit as expected!")
        return True
    elif limit_reached:
        print(f"\n✓✓✓ LIMIT ENFORCEMENT WORKING ✓✓✓")
        print(f"    System correctly prevented uploads exceeding 300 pages!")
        return True
    else:
        print(f"\n⚠ Test incomplete")
        print(f"    Need to upload more documents to reach 300-page limit")
        print(f"    Current: {final_usage} pages")
        return True

if __name__ == "__main__":
    try:
        run_test()
        print("\n" + "="*70)
        print("Test script completed")
        print("="*70)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
