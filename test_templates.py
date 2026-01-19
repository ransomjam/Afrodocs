import requests
import json
import os

API_BASE = 'http://localhost:5000'
session = requests.Session()

# First, login
print("Logging in...")
login_response = session.post(f'{API_BASE}/api/auth/login', json={
    'username': 'admin',
    'password': 'admin@secure123'
})

if login_response.status_code != 200:
    print(f"Login failed: {login_response.text}")
    exit(1)

if login_response.status_code == 200:
    print("✓ Login successful")
else:
    print(f"✗ Login failed: {login_response.text}")

# Test data for each institution
test_cases = [
    {
        'name': 'Bamenda (UBA)',
        'institution': 'uba',
        'faculty': 'College of Technology',
        'department': 'Computer Engineering',
        'document_type': 'Assignment'
    },
    {
        'name': 'Buea (UB)',
        'institution': 'ub',
        'faculty': 'Faculty of Science',
        'department': 'Department of Geology',
        'document_type': 'Thesis'
    },
    {
        'name': 'NPUI',
        'institution': 'npui',
        'faculty': 'School of Applied Sciences',
        'department': 'Information Technology',
        'document_type': 'Research Proposal'
    }
]

print("Testing Template Selection for Each Institution")
print("=" * 60)

for test in test_cases:
    print(f"\nTesting: {test['name']}")
    print(f"Institution ID: {test['institution']}")
    print(f"Document Type: {test['document_type']}")
    
    payload = {
        'institution': test['institution'],
        'faculty': test['faculty'],
        'department': test['department'],
        'documentType': test['document_type'],
        'studentName': 'John Doe',
        'studentId': 'TEST001',
        'title': 'Test Cover Page',
        'supervisor': 'Dr. Smith' if test['document_type'] in ['Thesis', 'Research Proposal'] else None,
        'instructor': 'Prof. Johnson' if test['document_type'] == 'Assignment' else None
    }
    
    try:
        response = session.post(f'{API_BASE}/api/coverpage/generate', json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                filename = data.get('filename', 'Unknown')
                print(f"✓ SUCCESS: Generated {filename}")
                
                # Check which template folder was used by examining the generated file path
                if 'Cover Pages_University of Bamenda' in str(data):
                    print("  Template Folder: University of Bamenda")
                elif 'Cover Page_University of Buea' in str(data):
                    print("  Template Folder: University of Buea")
                elif 'Cover Pages_National University Institute' in str(data):
                    print("  Template Folder: NPUI")
            else:
                print(f"✗ FAILED: {data.get('error', 'Unknown error')}")
        else:
            print(f"✗ HTTP Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"✗ Exception: {str(e)}")

print("\n" + "=" * 60)
print("Testing Complete!")
