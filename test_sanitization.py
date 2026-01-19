"""Test sanitization fix for corrupted input"""
import os
import sys
from docx import Document

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))
from coverpage_generator import generate_cover_page

# Test with corrupted data (simulating what's being sent)
corrupted_data = {
    'university': 'Bamenda',
    'documentType': 'Dissertation',
    'studentName': 'Jam Ransom',
    'studentId': 'UBa25PP227',
    'institution': 'College of Technology',
    'faculty': 'Faculty of Engineering and Technology',
    'department': 'Electrical and Electronic Engineering',
    'level': '400 Level',
    'supervisor': 'hjh',  # Corrupted data
    'academicSupervisor': 'hjh',
    'fieldSupervisor': '',
    'title': 'uiuiuiu',  # Corrupted title
    'monthYear': 'January 2026'
}

print("Testing with corrupted data...")
print(f"Input title: {repr(corrupted_data['title'])}")
print(f"Input supervisor: {repr(corrupted_data['supervisor'])}")

result = generate_cover_page(corrupted_data)
doc_path = result[0] if isinstance(result, tuple) else result

if doc_path and os.path.exists(doc_path):
    print(f"\n[OK] Document generated: {os.path.basename(doc_path)}")
    
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
    
    if 'uiuiuiu' in all_text:
        print("[WARNING] Corrupted data still present in document")
    else:
        print("[OK] Corrupted data was filtered out")
        
    if 'hjh' in all_text:
        print("[WARNING] Supervisor corruption still present")
    else:
        print("[OK] Supervisor corruption was filtered out")
        
    if '{{' in all_text:
        print("[WARNING] Placeholder markers still present")
    else:
        print("[OK] No placeholder markers")
else:
    error = result[1] if isinstance(result, tuple) else "Unknown"
    print(f"[ERROR] {error}")
