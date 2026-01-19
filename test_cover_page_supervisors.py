#!/usr/bin/env python3
"""
Test cover page field replacement with the new template
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from coverpage_generator import generate_cover_page

# Test data
test_data = {
    'documentType': 'Dissertation',
    'studentName': 'John Doe',
    'studentId': 'STU001',
    'department': 'Management',
    'faculty': 'Higher Institute of Commerce and Management',
    'title': 'Impact of Digital Marketing on Sales Performance',
    'supervisor': 'Dr. Jane Smith',
    'coSupervisor': 'Dr. Robert Johnson',
    'fieldSupervisor': 'Dr. Robert Johnson',
    'date': '2025-01-15'
}

print("Testing cover page generation with supervisor fields...")
print("=" * 60)
print("")
print("Test Data:")
for key, value in test_data.items():
    print(f"  {key}: {value}")

print("")
print("Generating cover page...")
output_path, error = generate_cover_page(test_data)

if error:
    print(f"ERROR: {error}")
else:
    print(f"SUCCESS: Cover page generated at: {output_path}")
    
    # Verify the content
    from docx import Document
    from docx.oxml.ns import qn
    
    doc = Document(output_path)
    
    print("")
    print("Verification - checking for supervisor fields in generated document:")
    print("-" * 60)
    
    found_supervisor = False
    found_cosupervisor = False
    
    # Check paragraphs
    for para in doc.paragraphs:
        if 'Smith' in para.text:
            print(f"Found Supervisor in paragraph: {para.text[:100]}")
            found_supervisor = True
        if 'Johnson' in para.text:
            print(f"Found Co-Supervisor in paragraph: {para.text[:100]}")
            found_cosupervisor = True
    
    # Check textboxes (more likely location in Word templates)
    if doc.element.body is not None:
        for txbx in doc.element.body.iter(qn('w:txbxContent')):
            for p in txbx.iter(qn('w:p')):
                full_text = ''
                for r in p.iter(qn('w:r')):
                    for t in r.iter(qn('w:t')):
                        if t.text:
                            full_text += t.text
                if 'Smith' in full_text:
                    print(f"Found Supervisor in textbox: {full_text[:100]}")
                    found_supervisor = True
                if 'Johnson' in full_text:
                    print(f"Found Co-Supervisor in textbox: {full_text[:100]}")
                    found_cosupervisor = True
    
    if found_supervisor and found_cosupervisor:
        print("")
        print("SUCCESS: All supervisor fields properly replaced!")
    else:
        print("")
        print("FAILURE: Some supervisor fields not properly replaced")
        if not found_supervisor:
            print("  - Supervisor name not found")
        if not found_cosupervisor:
            print("  - Co-supervisor name not found")
