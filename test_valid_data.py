"""Verify sanitization doesn't break valid data"""
import os
import sys
from docx import Document

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))
from coverpage_generator import generate_cover_page

# Test with valid data
valid_data = {
    'university': 'Bamenda',
    'documentType': 'Dissertation',
    'studentName': 'Jam Ransom',
    'studentId': 'UBa25PP227',
    'institution': 'College of Technology',
    'faculty': 'Faculty of Engineering and Technology',
    'department': 'Electrical and Electronic Engineering',
    'level': '400 Level',
    'supervisor': 'Prof. Dr. Emmanuel Tanyi',
    'academicSupervisor': 'Prof. Dr. Emmanuel Tanyi',
    'fieldSupervisor': 'Dr. Bernard Ngu',
    'title': 'Wireless Power Transfer Systems',  # Valid title
    'monthYear': 'January 2026'
}

print("Testing with VALID data...")
print(f"Input title: {repr(valid_data['title'])}")
print(f"Input supervisor: {repr(valid_data['supervisor'])}")

result = generate_cover_page(valid_data)
doc_path = result[0] if isinstance(result, tuple) else result

if doc_path and os.path.exists(doc_path):
    print(f"\n[OK] Document generated")
    
    doc = Document(doc_path)
    all_text = " ".join([p.text for p in doc.paragraphs])
    if doc.element.body is not None:
        for txbx in doc.element.body.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent'):
            for p in txbx.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                for r in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                    for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                        if t.text:
                            all_text += " " + t.text
    
    checks = {
        'Title Present': 'Wireless' in all_text,
        'Supervisor Present': 'Emmanuel' in all_text,
        'Field Supervisor Present': 'Bernard' in all_text,
        'Student Name Present': 'Jam Ransom' in all_text,
        'No Placeholders': '{{' not in all_text,
    }
    
    for check, result in checks.items():
        status = "[OK]" if result else "[FAIL]"
        print(f"  {status} {check}")
else:
    error = result[1] if isinstance(result, tuple) else "Unknown"
    print(f"[ERROR] {error}")
