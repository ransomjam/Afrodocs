import requests
from docx import Document
import os
from datetime import datetime
import time

API_BASE = 'http://localhost:5000'
session = requests.Session()

# Login
login_response = session.post(f'{API_BASE}/api/auth/login', json={
    'username': 'admin',
    'password': 'admin@secure123'
})

if login_response.status_code != 200:
    print(f"Login failed!")
    exit(1)

print("✓ Logged in\n")

# Define template file sizes (known from directory listing)
template_sizes = {
    'bamenda_assignment': 75969,
    'buea_assignment': 214608,
    'npui_assignment': 109933,
    'bamenda_thesis': 75653,
    'buea_thesis': 214581,
    'npui_thesis': 109785,
    'bamenda_research': 80093,
    'buea_research': 215991,
    'npui_research': 114471,
}

# Test data
test_cases = [
    {
        'name': 'Bamenda (UBA)',
        'institution': 'uba',
        'faculty': 'College of Technology',
        'department': 'Computer Engineering',
        'document_type': 'Assignment',
        'expected_size_range': (75000, 76000)
    },
    {
        'name': 'Buea (UB)',
        'institution': 'ub',
        'faculty': 'Faculty of Science',
        'department': 'Department of Geology',
        'document_type': 'Thesis',
        'expected_size_range': (214000, 215000)
    },
    {
        'name': 'NPUI',
        'institution': 'npui',
        'faculty': 'School of Applied Sciences',
        'department': 'Information Technology',
        'document_type': 'Research Proposal',
        'expected_size_range': (114000, 115000)
    }
]

output_dir = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\backend\outputs"

print("=" * 80)
print("TEMPLATE SELECTION VERIFICATION BY FILE SIZE")
print("=" * 80)

for test in test_cases:
    print(f"\n{test['name']} ({test['institution']})")
    print(f"Document Type: {test['document_type']}")
    print(f"Expected File Size: {test['expected_size_range'][0]} - {test['expected_size_range'][1]} bytes")
    
    payload = {
        'institution': test['institution'],
        'faculty': test['faculty'],
        'department': test['department'],
        'documentType': test['document_type'],
        'studentName': 'Test Student',
        'studentId': 'TEST2026',
        'title': f'Size Test {test["name"]}',
        'supervisor': 'Dr. Smith' if test['document_type'] in ['Thesis', 'Research Proposal'] else None,
        'instructor': 'Prof. Johnson' if test['document_type'] == 'Assignment' else None
    }
    
    response = session.post(f'{API_BASE}/api/coverpage/generate', json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            job_id = data.get('job_id')
            
            time.sleep(0.3)
            expected_file = os.path.join(output_dir, f"{job_id}_formatted.docx")
            
            if os.path.exists(expected_file):
                file_size = os.path.getsize(expected_file)
                print(f"  Actual File Size: {file_size} bytes")
                
                min_size, max_size = test['expected_size_range']
                if min_size <= file_size <= max_size:
                    print(f"  ✓ CORRECT TEMPLATE: File size matches expected range")
                elif 75000 <= file_size <= 76000:
                    print(f"  ✗ WRONG TEMPLATE: Using Bamenda template instead")
                elif 214000 <= file_size <= 215000:
                    print(f"  ✗ WRONG TEMPLATE: Using Buea template instead")
                elif 109000 <= file_size <= 115000:
                    print(f"  ✗ WRONG TEMPLATE: Using NPUI template instead")
                else:
                    print(f"  ? UNKNOWN: File size doesn't match any known template")
            else:
                print(f"  ✗ File not found")
        else:
            print(f"  ✗ Generation failed: {data.get('error')}")
    else:
        print(f"  ✗ API error: {response.status_code}")

print("\n" + "=" * 80)
print("VERIFICATION COMPLETE!")
print("=" * 80)
