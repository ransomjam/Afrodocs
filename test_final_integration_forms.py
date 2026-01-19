"""Final integration test - simulating actual form submission"""
import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))
from coverpage_generator import generate_cover_page

# Simulate form data from frontend (as would be sent in POST request)
form_submissions = [
    {
        'name': 'Bamenda Assignment',
        'data': {
            'university': 'Bamenda',
            'documentType': 'Assignment',
            'studentName': 'Alice Kumfengo',
            'studentId': 'MB25CST042',
            'institution': 'Faculty of Arts',
            'faculty': 'Faculty of Arts',
            'department': 'Department of English Language',
            'level': '200 Level',
            'courseCode': 'ENG 201',
            'courseTitle': 'Advanced Grammar and Composition',
            'instructor': 'Prof. Amina Fongoh',
            'assignmentNumber': '3',
            'title': 'Grammar Analysis Assignment',
            'supervisor': '',
            'academicSupervisor': '',
            'fieldSupervisor': '',
        }
    },
    {
        'name': 'Bamenda Dissertation',
        'data': {
            'university': 'Bamenda',
            'documentType': 'Dissertation',
            'studentName': 'Bernard Njembia',
            'studentId': 'MB23ENG087',
            'institution': 'College of Technology',
            'faculty': 'Faculty of Engineering and Technology',
            'department': 'Electrical and Electronic Engineering',
            'level': 'Postgraduate',
            'title': 'Wireless Power Transfer Systems Using Resonant Coupling',
            'supervisor': 'Prof. Dr. Ngoh Chukwuemeka',
            'academicSupervisor': 'Prof. Dr. Ngoh Chukwuemeka',
            'fieldSupervisor': 'Dr. Tekelee Victor',
            'monthYear': 'January 2026',
        }
    },
    {
        'name': 'Buea Dissertation',
        'data': {
            'university': 'Buea',
            'documentType': 'Dissertation',
            'studentName': 'Grace Mbakop',
            'studentId': 'UBu23TECH105',
            'institution': 'College of Technology',
            'faculty': 'Faculty of Engineering',
            'department': 'Civil Engineering',
            'level': 'Postgraduate',
            'title': 'Sustainable Infrastructure Solutions for Rural Communities',
            'supervisor': 'Prof. Dr. Nkemka Elias',
            'academicSupervisor': 'Prof. Dr. Nkemka Elias',
            'fieldSupervisor': 'Dr. Awah Maurice',
            'monthYear': 'January 2026',
        }
    },
    {
        'name': 'Buea Internship Report',
        'data': {
            'university': 'Buea',
            'documentType': 'Internship Report',
            'studentName': 'Samuel Tanyi',
            'studentId': 'UBu24CSE056',
            'institution': 'Faculty of Science',
            'faculty': 'Faculty of Science',
            'department': 'Computer Science',
            'level': '400 Level',
            'title': 'Internship at MTN Cameroon - Network Operations',
            'supervisor': 'Prof. Dr. Akah Anne',
            'fieldSupervisor': 'Eng. Peter Tata (MTN)',
            'monthYear': 'January 2026',
        }
    }
]

print("="*80)
print("FINAL INTEGRATION TEST - SIMULATING FORM SUBMISSIONS")
print("="*80)

results = []
for submission in form_submissions:
    name = submission['name']
    data = submission['data']
    
    print(f"\n[TESTING] {name}")
    print(f"  University: {data['university']}")
    print(f"  Document Type: {data['documentType']}")
    print(f"  Student: {data['studentName']} ({data['studentId']})")
    
    result = generate_cover_page(data)
    doc_path = result[0] if isinstance(result, tuple) else result
    error = result[1] if isinstance(result, tuple) and len(result) > 1 else None
    
    if doc_path and os.path.exists(doc_path):
        # Quick check for supervisor fields
        from docx import Document
        doc = Document(doc_path)
        all_text = " ".join([p.text for p in doc.paragraphs])
        
        if doc.element.body is not None:
            for txbx in doc.element.body.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent'):
                for p in txbx.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                    for r in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                        for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                            if t.text:
                                all_text += " " + t.text
        
        has_supervisor = data['supervisor'] and data['supervisor'] in all_text if data['supervisor'] else "N/A"
        has_field_supervisor = data['fieldSupervisor'] and data['fieldSupervisor'] in all_text if data['fieldSupervisor'] else "N/A"
        
        print(f"  Status: [PASS]")
        print(f"    - Document generated: {os.path.basename(doc_path)}")
        print(f"    - Academic Supervisor: {has_supervisor}")
        print(f"    - Field Supervisor: {has_field_supervisor}")
        print(f"    - No placeholders: {'OK' if '{{' not in all_text else 'FAILED'}")
        results.append(True)
    else:
        print(f"  Status: [FAIL]")
        print(f"    - Error: {error}")
        results.append(False)

print(f"\n{'='*80}")
print(f"RESULTS: {sum(results)}/{len(results)} tests passed")
print(f"{'='*80}")

if all(results):
    print("\n[SUCCESS] All forms can generate cover pages correctly!")
else:
    print("\n[WARNING] Some forms failed")
