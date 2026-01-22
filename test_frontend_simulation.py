#!/usr/bin/env python3
"""
Test that simulates exact frontend behavior step-by-step
"""
import requests
import json
import sys

BASE_URL = "http://localhost:5000"
session = requests.Session()

print("="*70)
print("SIMULATING EXACT FRONTEND BEHAVIOR")
print("="*70)

# Step 1: Authenticate exactly as frontend does
print("\n1. Login...")
try:
    login_resp = session.post(
        f"{BASE_URL}/api/auth/login",
        json={'username': 'admin', 'password': 'admin@secure123'}
    )
    if login_resp.status_code != 200:
        print(f"❌ Login failed: {login_resp.status_code}")
        sys.exit(1)
    print(f"✅ Authenticated")
except Exception as e:
    print(f"❌ Exception during login: {e}")
    sys.exit(1)

# Step 2: Send form data exactly as frontend does
print("\n2. Sending coverpage form (simulating frontend form data)...")

# This is the exact format the frontend sends
form_data = {
    'university': 'Bamenda',
    'documentType': 'Assignment',
    'studentName': 'John Doe',
    'studentId': 'MB24000001',
    'courseCode': 'CS301',
    'courseTitle': 'Software Engineering',
    'institution': 'College of Technology',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'level': '300 Level',
    'instructor': 'Dr. Nkengasong',
    'date': '2025-01-20',
    'title': 'Software Design Principles'
}

# Frontend adds mergeJobId to the form data if merging
# For standalone, it's not included or is None
payload = {**form_data, 'mergeJobId': None}

print(f"   Payload keys: {list(payload.keys())}")
print(f"   Sending to: POST /api/coverpage/generate")

try:
    response = session.post(
        f"{BASE_URL}/api/coverpage/generate",
        json=payload,
        headers={'Content-Type': 'application/json'},
        timeout=30
    )
    
    print(f"   Response status: {response.status_code}")
    print(f"   Response size: {len(response.content)} bytes")
    
    # Parse response exactly as frontend does
    data = response.json()
    print(f"   Response JSON keys: {list(data.keys())}")
    
    # Frontend checks:  if (data.success)
    if data.get('success'):
        print(f"✅ Response success: TRUE")
        print(f"   - job_id: {data.get('job_id')}")
        print(f"   - filename: {data.get('filename')}")
        print(f"   - is_merged: {data.get('is_merged')}")
        
        # Frontend does:  const pdfFilename = data.filename ? data.filename.replace(/\.docx$/i, '.pdf') : 'formatted_document.pdf';
        pdf_filename = data['filename'].replace('.docx', '.pdf') if data.get('filename') else 'formatted_document.pdf'
        print(f"   - PDF filename would be: {pdf_filename}")
        
        # Frontend does: const previewUrl = `${API_BASE}/download-pdf/${data.job_id}/${encodeURIComponent(pdfFilename)}?inline=true`;
        preview_url = f"{BASE_URL}/download-pdf/{data['job_id']}/{pdf_filename}?inline=true"
        print(f"   - Preview URL would be: {preview_url}")
        
        print(f"\n✅ FRONTEND WOULD ACCEPT THIS RESPONSE")
    else:
        print(f"❌ Response success: FALSE")
        print(f"   - error: {data.get('error')}")
        
except json.JSONDecodeError as e:
    print(f"❌ Failed to parse JSON: {e}")
    print(f"   Response text: {response.text[:200]}")
except Exception as e:
    print(f"❌ Exception: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("FRONTEND SIMULATION TEST COMPLETE")
print("="*70)
