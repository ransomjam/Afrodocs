import requests
import json

API_BASE = 'http://localhost:5000'
session = requests.Session()

# Login
print("Logging in...")
login_response = session.post(f'{API_BASE}/api/auth/login', json={
    'username': 'admin',
    'password': 'admin@secure123'
})

if login_response.status_code != 200:
    print(f"Login failed!")
    exit(1)

print("✓ Logged in\n")

# Test just Bamenda
payload = {
    'institution': 'uba',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'documentType': 'Assignment',
    'studentName': 'Test Student',
    'studentId': 'TEST2026',
    'title': 'Test Title',
    'instructor': 'Prof. Test'
}

print("Sending request to generate cover page...")
print(f"Payload: {json.dumps(payload, indent=2)}\n")

response = session.post(f'{API_BASE}/api/coverpage/generate', json=payload)

print(f"Response Status: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")
print(f"Response Body:\n{response.text}\n")

if response.status_code == 200:
    data = response.json()
    print(f"Success: {data.get('success')}")
    print(f"Filename: {data.get('filename')}")
    print(f"Job ID: {data.get('job_id')}")
    if not data.get('success'):
        print(f"Error: {data.get('error')}")
