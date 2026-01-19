#!/usr/bin/env python
"""
Direct test of placeholder replacement fix
Tests the coverpage_generator.generate_cover_page function directly
"""

import os
import sys
from docx import Document
from docx.oxml.ns import qn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter/backend'))

# Suppress Flask startup
os.environ['FLASK_ENV'] = 'testing'

from coverpage_generator import generate_cover_page

def extract_all_text(doc_path):
    """Extract all text from document including textboxes"""
    doc = Document(doc_path)
    all_text = []
    
    # From paragraphs
    for p in doc.paragraphs:
        all_text.append(p.text)
    
    # From textboxes
    if doc.element.body is not None:
        for txbx in doc.element.body.iter(qn('w:txbxContent')):
            for p in txbx.iter(qn('w:p')):
                full_p_text = ''
                for r in p.iter(qn('w:r')):
                    for t in r.iter(qn('w:t')):
                        if t.text:
                            full_p_text += t.text
                if full_p_text:
                    all_text.append(full_p_text)
    
    return all_text

def test_placeholder_fix():
    """Test that placeholders are properly replaced"""
    print("\n" + "="*70)
    print("PLACEHOLDER REPLACEMENT FIX TEST")
    print("="*70)
    
    test_data = {
        'documentType': 'Internship Report',
        'institution': 'Royal Institute',
        'faculty': 'Faculty of Science',
        'department': 'Advanced Computing',
        'level': '400 Level',
        'studentName': 'Jane Smith',
        'studentId': 'ENG001',
        'title': 'Advanced Practicum Report',
        'supervisor': 'Dr. Michael Brown',
        'coSupervisor': 'Prof. Sarah Johnson',
        'date': '2026-01-15'
    }
    
    try:
        print("\n1. Generating cover page...")
        output_path, error = generate_cover_page(test_data)
        
        if error:
            print(f"[FAIL] Error: {error}")
            return False
        
        if not os.path.exists(output_path):
            print(f"[FAIL] File not created: {output_path}")
            return False
        
        print(f"[OK] Generated: {os.path.basename(output_path)}")
        
        # Extract text
        print("\n2. Extracting document content...")
        all_text = extract_all_text(output_path)
        full_document = '\n'.join(all_text)
        
        # Check for problems
        print("\n3. Checking for placeholder merging issues...\n")
        
        issues_found = []
        
        # Issue 1: Remaining placeholder markers
        if '{{' in full_document or '}}' in full_document:
            import re
            remaining = re.findall(r'\{\{[^}]*\}\}', full_document)
            if remaining:
                issues_found.append(f"Remaining placeholders: {remaining}")
        
        # Issue 2: Merged patterns like "{{ReportTitleREPORT TITLE}}"
        if 'Schoo/Faculty' in full_document:
            print("[WARN] Found 'Schoo/Faculty' - checking for merger...")
            # Check if it's a standalone line (OK) or merged with other text (BAD)
            for line in all_text:
                if 'Schoo/Faculty' in line and len(line) < 50:
                    print(f"  Found standalone: '{line}'")
                elif 'Schoo/Faculty' in line:
                    print(f"  [POTENTIAL ISSUE] Line too long: '{line[:100]}'")
                    if 'Schoo/FacultyFaculty of Science' in line or 'Schoo/Faculty' in line and 'Faculty of' in line and '{{' not in line:
                        issues_found.append(f"Possible merged pattern: {line[:60]}")
        
        # Issue 3: Check for the specific patterns mentioned
        if '{{REPORT TITLE' in full_document or 'REPORT TITLEADVANCED' in full_document or 'REPORT TITLEPRACTICUM' in full_document:
            issues_found.append("Found REPORT TITLE merger pattern")
        
        if '{{Schoo/Faculty' in full_document or 'Schoo/FacultyFaculty of' in full_document:
            issues_found.append("Found Schoo/Faculty merger pattern")
        
        # Print results
        print("\n4. Test Results:")
        print("="*70)
        
        if issues_found:
            print("[FAIL] Placeholder merging detected:")
            for issue in issues_found:
                print(f"  ERROR: {issue}")
            
            print("\nDocument content (first 20 lines):")
            for i, line in enumerate(all_text[:20]):
                print(f"  [{i}] {line[:80]}")
            
            return False
        else:
            print("[PASS] No placeholder merging detected")
            print("[PASS] All placeholders properly replaced")
            
            print("\nDocument content preview (non-empty lines):")
            content_lines = [line for line in all_text if line.strip() and len(line) > 5]
            for line in content_lines[:15]:
                # Show key values
                if any(x in line.upper() for x in ['FACULTY', 'DEPARTMENT', 'REPORT', 'ADVANCED', 'JANE', 'BROWN']):
                    print(f"  OK: {line[:80]}")
            
            print(f"\n[SUCCESS] Test passed!")
            print(f"Generated: {os.path.basename(output_path)}")
            return True
        
    except Exception as e:
        print(f"[FAIL] Exception: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    result = test_placeholder_fix()
    sys.exit(0 if result else 1)
