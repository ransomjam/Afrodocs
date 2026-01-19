"""Debug the scattered layout and corrupted title issue"""
import os
import sys
from docx import Document

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))
from coverpage_generator import generate_cover_page

# Test with the exact data that produces the issue
test_data = {
    'university': 'Bamenda',
    'documentType': 'Dissertation',
    'studentName': 'Jam Ransom',
    'studentId': 'UBa25PP227',
    'institution': 'College of Technology',
    'faculty': 'Faculty of Engineering and Technology',
    'department': 'Electrical and Electronic Engineering',
    'level': '400 Level',
    'supervisor': 'Prof. Dr. John Smith',  # Try with supervisor
    'academicSupervisor': 'Prof. Dr. John Smith',
    'fieldSupervisor': 'Dr. Field Supervisor',
    'title': '',  # Empty title - might be the issue
    'monthYear': 'January 2026'
}

print("Testing with potentially problematic data...")
print(f"Title: '{test_data['title']}' (length: {len(test_data['title'])})")

result = generate_cover_page(test_data)
doc_path = result[0] if isinstance(result, tuple) else result

if doc_path and os.path.exists(doc_path):
    print(f"\nGenerated: {doc_path}")
    doc = Document(doc_path)
    
    print("\n=== TEXTBOX CONTENT ANALYSIS ===")
    if doc.element.body is not None:
        textbox_num = 0
        for txbx in doc.element.body.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent'):
            textbox_num += 1
            para_text = ""
            for p in txbx.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                for r in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                    for t in r.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                        if t.text:
                            para_text += t.text
            
            if para_text.strip():
                # Show detailed info
                print(f"TB{textbox_num}: [{len(para_text)} chars] {repr(para_text[:50])}")
                
                # Check for corrupted/garbage text
                if not any(c.isalpha() for c in para_text) or para_text.strip() in ['uuiuiu', 'iiiiiii']:
                    print(f"  [ALERT] Corrupted text detected!")
else:
    error = result[1] if isinstance(result, tuple) else "Unknown"
    print(f"ERROR: {error}")
