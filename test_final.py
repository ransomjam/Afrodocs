import requests
from docx import Document
import os
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

# Test data
test_cases = [
    {
        'name': 'Bamenda (UBA)',
        'institution': 'uba',
        'faculty': 'College of Technology',
        'department': 'Computer Engineering',
        'document_type': 'Assignment',
        'expected_min': 60000,
        'expected_max': 75000
    },
    {
        'name': 'Buea (UB)',
        'institution': 'ub',
        'faculty': 'Faculty of Science',
        'department': 'Department of Geology',
        'document_type': 'Thesis',
        'expected_min': 200000,
        'expected_max': 215000
    },
    {
        'name': 'NPUI',
        'institution': 'npui',
        'faculty': 'School of Applied Sciences',
        'department': 'Information Technology',
        'document_type': 'Research Proposal',
        'expected_min': 105000,
        'expected_max': 120000
    }
]

output_dir = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\backend\outputs"

print("=" * 80)
print("TEMPLATE SELECTION VERIFICATION")
print("=" * 80)

results = []
for test in test_cases:
    print(f"\n{test['name']} ({test['institution']})")
    print(f"Document Type: {test['document_type']}")
    
    payload = {
        'institution': test['institution'],
        'faculty': test['faculty'],
        'department': test['department'],
        'documentType': test['document_type'],
        'studentName': 'Test Student',
        'studentId': 'TEST2026',
        'title': f'Template Verification {test["name"]}',
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
                print(f"  File Size: {file_size} bytes")
                print(f"  Expected Range: {test['expected_min']}-{test['expected_max']} bytes")
                
                if test['expected_min'] <= file_size <= test['expected_max']:
                    print(f"  ✅ SUCCESS: Using correct {test['name']} template!")
                    results.append((test['name'], 'PASS'))
                else:
                    print(f"  ❌ FAIL: File size outside expected range")
                    results.append((test['name'], 'FAIL'))
            else:
                print(f"  ✗ File not found")
                results.append((test['name'], 'ERROR'))
        else:
            print(f"  ✗ Generation failed: {data.get('error')}")
            results.append((test['name'], 'ERROR'))
    else:
        print(f"  ✗ API error: {response.status_code}")
        results.append((test['name'], 'ERROR'))

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
for name, status in results:
    symbol = "✅" if status == "PASS" else "❌"
    print(f"{symbol} {name}: {status}")

all_pass = all(status == 'PASS' for _, status in results)
print("\n" + ("=" * 80))
if all_pass:
    print("🎉 ALL TESTS PASSED! Template mapping is working correctly!")
else:
    print("⚠️ Some tests failed. Please review.")
print("=" * 80)
