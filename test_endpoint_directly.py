#!/usr/bin/env python3
"""
Direct test of the coverpage endpoint to diagnose the issue.
"""
import requests
import json
import os
import sys
import time

# Flask app is running on localhost:5000
BASE_URL = "http://localhost:5000"

# Create a session to maintain cookies
session = requests.Session()

# Test data - matches what the frontend sends
test_data = {
    'university': 'Bamenda',
    'documentType': 'Assignment',
    'studentName': 'Test Student',
    'studentId': 'TEST001',
    'courseCode': 'TEST101',
    'courseTitle': 'Test Course',
    'institution': 'College of Technology',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'level': '300 Level',
    'instructor': 'Prof. Test',
    'date': '2025-01-15',
    'title': 'Test Cover Page',
    'mergeJobId': None  # Standalone
}

print(f"\n📋 Testing coverpage endpoint directly")
print(f"Base URL: {BASE_URL}")

# Step 1: Login
print("\n" + "="*60)
print("STEP 1: Authenticate")
print("="*60)

try:
    print(f"\nPOST {BASE_URL}/api/auth/login")
    login_response = session.post(
        f"{BASE_URL}/api/auth/login",
        json={
            'username': 'admin',
            'password': 'admin@secure123'
        },
        timeout=10
    )
    
    print(f"Login Status: {login_response.status_code}")
    if login_response.status_code == 200:
        login_data = login_response.json()
        if login_data.get('message') or not login_data.get('error'):
            print(f"✅ Logged in successfully")
            print(f"   User: {login_data.get('username')}")
        else:
            print(f"❌ Login failed: {login_data.get('error')}")
            sys.exit(1)
    else:
        print(f"❌ Login error: {login_response.text}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Login exception: {e}")
    sys.exit(1)

# Test 1: Generate standalone coverpage
print("\n" + "="*60)
print("TEST 1: Generate Standalone Coverpage (JSON)")
print("="*60)

try:
    print(f"\nPOST {BASE_URL}/api/coverpage/generate")
    print(f"Content-Type: application/json")
    print(f"Payload:")
    print(json.dumps(test_data, indent=2))
    
    response = session.post(
        f"{BASE_URL}/api/coverpage/generate",
        json=test_data,  # Send as JSON
        timeout=30
    )
    
    print(f"\n📨 Response Status: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Content-Length: {len(response.content)} bytes")
    
    try:
        response_json = response.json()
        print(f"\n✓ Response JSON:")
        print(json.dumps(response_json, indent=2))
        
        if response_json.get('success'):
            print(f"\n✅ SUCCESS! Endpoint returned success!")
            job_id = response_json.get('job_id')
            print(f"  Job ID: {job_id}")
            print(f"  Filename: {response_json.get('filename')}")
            print(f"  Is Merged: {response_json.get('is_merged')}")
            print(f"  Download URL: {response_json.get('downloadUrl')}")
            
            # Try to download
            print(f"\n📥 Attempting to download...")
            time.sleep(1)
            download_response = session.get(
                f"{BASE_URL}/download/{job_id}",
                timeout=30
            )
            print(f"Download status: {download_response.status_code}")
            if download_response.status_code == 200:
                print(f"✅ Download successful ({len(download_response.content)} bytes)")
            else:
                print(f"❌ Download failed: {download_response.text[:200]}")
        else:
            print(f"\n❌ ERROR! Endpoint returned success=false")
            print(f"  Error: {response_json.get('error')}")
                
    except json.JSONDecodeError as e:
        print(f"\n❌ Failed to parse response as JSON: {e}")
        print(f"Response text: {response.text[:500]}")
            
except Exception as e:
    print(f"❌ Error during test: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("Test complete")
print("="*60)
