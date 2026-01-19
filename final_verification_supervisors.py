"""Final verification - all supervisor scenarios"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))
from coverpage_generator import generate_cover_page
from docx import Document

print("="*80)
print("FINAL VERIFICATION - SUPERVISOR FIELD HANDLING")
print("="*80)

test_cases = [
    {
        'name': 'With Academic Supervisor Only',
        'data': {
            'university': 'Bamenda',
            'documentType': 'Dissertation',
            'studentName': 'Test Student 1',
            'studentId': 'MB26T001',
            'institution': 'College of Technology',
            'faculty': 'Faculty of Engineering',
            'department': 'Computer Science',
            'level': 'Postgraduate',
            'title': 'Test Dissertation 1',
            'supervisor': 'Prof. Dr. John Smith',
            'academicSupervisor': 'Prof. Dr. John Smith',
            'fieldSupervisor': '',  # Empty
        }
    },
    {
        'name': 'With Both Supervisors',
        'data': {
            'university': 'Buea',
            'documentType': 'Dissertation',
            'studentName': 'Test Student 2',
            'studentId': 'UBu26T002',
            'institution': 'Faculty of Science',
            'faculty': 'Faculty of Science',
            'department': 'Biology',
            'level': 'Postgraduate',
            'title': 'Test Dissertation 2',
            'supervisor': 'Prof. Dr. Mary Johnson',
            'academicSupervisor': 'Prof. Dr. Mary Johnson',
            'fieldSupervisor': 'Dr. Peter Williams',
        }
    },
    {
        'name': 'Internship with Different Supervisor',
        'data': {
            'university': 'Bamenda',
            'documentType': 'Internship Report',
            'studentName': 'Test Student 3',
            'studentId': 'MB26T003',
            'institution': 'Faculty of Arts',
            'faculty': 'Faculty of Arts',
            'department': 'English',
            'level': '400 Level',
            'title': 'Internship Report',
            'supervisor': 'Prof. Dr. Anne Brown',
            'fieldSupervisor': 'Mr. Company Supervisor',
        }
    }
]

all_passed = True
for i, test_case in enumerate(test_cases, 1):
    print(f"\n[TEST {i}] {test_case['name']}")
    data = test_case['data']
    
    result = generate_cover_page(data)
    doc_path = result[0] if isinstance(result, tuple) else result
    
    if not doc_path or not os.path.exists(doc_path):
        print(f"  [FAIL] Document not generated")
        all_passed = False
        continue
    
    doc = Document(doc_path)
    
    # Extract all text
    all_text = " ".join([p.text for p in doc.paragraphs])
    if doc.element.body is not None:
        for txbx in doc.element.body.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent'):
            for p in txbx.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                for r in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                    for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                        if t.text:
                            all_text += " " + t.text
    
    # Check conditions
    checks = {
        'Document Generated': True,
        'No Placeholder Markers': '{{' not in all_text,
        'Student Name Present': data['studentName'] in all_text,
    }
    
    # Check supervisors based on what's provided
    if data['supervisor']:
        checks[f'Academic Supervisor: {data["supervisor"]}'] = data['supervisor'] in all_text
    
    if data.get('fieldSupervisor'):
        checks[f'Field Supervisor: {data["fieldSupervisor"]}'] = data['fieldSupervisor'] in all_text
    
    # Print results
    passed = all(checks.values())
    status = "[PASS]" if passed else "[FAIL]"
    print(f"  {status}")
    
    for check_name, result in checks.items():
        check_status = "[OK]" if result else "[FAIL]"
        print(f"    {check_status} {check_name}")
    
    if not passed:
        all_passed = False

print(f"\n{'='*80}")
if all_passed:
    print("RESULT: [SUCCESS] ALL SUPERVISOR SCENARIOS VERIFIED - SYSTEM READY")
else:
    print("RESULT: [FAILED] SOME TESTS FAILED - REVIEW NEEDED")
print(f"{'='*80}")
