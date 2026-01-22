#!/usr/bin/env python3
"""Quick direct test of coverpage endpoint"""
import requests
import json
import sys
import traceback

BASE = "http://localhost:5000"

try:
    s = requests.Session()
    
    print("1. Login...")
    sys.stdout.flush()
    r = s.post(f"{BASE}/api/auth/login", json={"username":"admin","password":"admin@secure123"}, timeout=5)
    print(f"   Status: {r.status_code}")
    if r.status_code != 200:
        print(f"   ERROR: {r.text}")
        exit(1)
    
    print("2. Generate coverpage...")
    sys.stdout.flush()
    payload = {
        'university': 'Bamenda',
        'documentType': 'Assignment',
        'studentName': 'Test',
        'studentId': '001',
        'courseCode': 'CS',
        'courseTitle': 'Test',
        'institution': 'College',
        'faculty': 'Faculty',
        'department': 'Dept',
        'level': '300',
        'instructor': 'Prof',
        'date': '2025-01-21',
        'title': 'Test Title'
    }
    
    r = s.post(f"{BASE}/api/coverpage/generate", json=payload, timeout=10)
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.text}")
    
    if r.status_code == 200:
        data = r.json()
        if data.get('success'):
            print(f"   ✅ SUCCESS: job_id={data.get('job_id')}")
        else:
            print(f"   ❌ FAILED: {data.get('error')}")
    else:
        print(f"   ❌ HTTP ERROR: {r.status_code}")

except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
