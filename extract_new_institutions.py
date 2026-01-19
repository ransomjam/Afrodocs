#!/usr/bin/env python3
"""
Extract schools/faculties/departments data from Word documents
for BUST and Catholic University
"""

from docx import Document
import json
from pathlib import Path

def extract_departments_from_docx(docx_path):
    """Extract departments structure from Word document"""
    doc = Document(docx_path)
    
    print(f"\n{'='*80}")
    print(f"Extracting from: {Path(docx_path).name}")
    print(f"{'='*80}")
    
    data = {
        'schools': []
    }
    
    current_school = None
    current_faculty = None
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
            
        # Get indentation level (approximate)
        indent = len(para.text) - len(para.text.lstrip())
        
        print(f"Indent: {indent:3d} | Text: {text[:80]}")
        
        # Try to identify structure based on indent level
        if indent == 0 and len(text) > 0:
            # School level
            current_school = {
                'name': text,
                'faculties': []
            }
            data['schools'].append(current_school)
            print(f"  → School: {text}")
            
        elif indent > 0 and current_school:
            # Could be faculty or department
            if ':' in text or '/' in text:
                # Likely a faculty with departments
                parts = text.split(':' if ':' in text else '/')
                faculty_name = parts[0].strip()
                
                faculty = {
                    'name': faculty_name,
                    'departments': []
                }
                
                # If there are departments in the same line
                if len(parts) > 1:
                    depts = [d.strip() for d in parts[1].split(',')]
                    faculty['departments'] = depts
                
                current_school['faculties'].append(faculty)
                current_faculty = faculty
                print(f"    → Faculty: {faculty_name}")
                if faculty['departments']:
                    print(f"       Departments: {faculty['departments']}")
            else:
                # Likely a department
                if current_faculty:
                    current_faculty['departments'].append(text)
                    print(f"       → Department: {text}")
    
    return data

# Extract BUST data
bust_doc = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages\Cover Page _ BUST\BUST _ Schools-Faculties-Departments.docx"
bust_data = extract_departments_from_docx(bust_doc)

# Extract Catholic University data
catholic_doc = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages\Cover Page _ Catholic University\Catholic University Of Cameroon, Bamenda _ Schools-Faculties-Departments.docx"
catholic_data = extract_departments_from_docx(catholic_doc)

print(f"\n{'='*80}")
print("BUST Data Summary:")
print(f"{'='*80}")
print(f"Schools: {len(bust_data['schools'])}")
for school in bust_data['schools']:
    print(f"  - {school['name']}")
    print(f"    Faculties: {len(school['faculties'])}")
    for fac in school['faculties']:
        print(f"      - {fac['name']}: {len(fac['departments'])} departments")

print(f"\n{'='*80}")
print("Catholic University Data Summary:")
print(f"{'='*80}")
print(f"Schools: {len(catholic_data['schools'])}")
for school in catholic_data['schools']:
    print(f"  - {school['name']}")
    print(f"    Faculties: {len(school['faculties'])}")
    for fac in school['faculties']:
        print(f"      - {fac['name']}: {len(fac['departments'])} departments")

# Save extracted data for reference
with open('extracted_bust_data.json', 'w', encoding='utf-8') as f:
    json.dump(bust_data, f, ensure_ascii=False, indent=2)

with open('extracted_catholic_data.json', 'w', encoding='utf-8') as f:
    json.dump(catholic_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Data saved to extracted_bust_data.json and extracted_catholic_data.json")
