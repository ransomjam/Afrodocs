#!/usr/bin/env python3
"""
Comprehensive test for cover page generation with all field types
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from coverpage_generator import generate_cover_page
from docx import Document
from docx.oxml.ns import qn

def test_comprehensive_cover_page():
    """Test all cover page field types"""
    
    print("=" * 70)
    print("COMPREHENSIVE COVER PAGE FIELD REPLACEMENT TEST")
    print("=" * 70)
    
    test_cases = [
        {
            'name': 'Dissertation with Co-Supervisor',
            'data': {
                'documentType': 'Dissertation',
                'studentName': 'Alice Emma Johnson',
                'studentId': 'DST20240156',
                'department': 'Business Administration',
                'faculty': 'Higher Institute of Commerce and Management',
                'title': 'Blockchain Technology in Supply Chain Management',
                'supervisor': 'Prof. Michael Chen',
                'coSupervisor': 'Dr. Sarah Williams',
                'date': '2025-01-15'
            }
        },
        {
            'name': 'Dissertation with Field Supervisor',
            'data': {
                'documentType': 'Dissertation',
                'studentName': 'Nathaniel Oscar Brown',
                'studentId': 'DST20240157',
                'department': 'Marketing',
                'faculty': 'Higher Institute of Commerce and Management',
                'title': 'Consumer Behavior in Digital Marketing Platforms',
                'supervisor': 'Dr. Jennifer Martinez',
                'fieldSupervisor': 'Prof. David Lee',
                'date': '2025-02-20'
            }
        }
    ]
    
    for test_case in test_cases:
        print("")
        print(f"Test: {test_case['name']}")
        print("-" * 70)
        
        output_path, error = generate_cover_page(test_case['data'])
        
        if error:
            print(f"ERROR: {error}")
            continue
        
        print(f"Generated: {os.path.basename(output_path)}")
        
        # Verify all fields
        doc = Document(output_path)
        data = test_case['data']
        
        fields_to_check = {
            'student_name': data['studentName'],
            'department': data['department'],
            'topic': data['title'],
            'supervisor': data.get('supervisor', ''),
            'co_supervisor': data.get('coSupervisor') or data.get('fieldSupervisor', '')
        }
        
        verified_fields = {}
        document_text = ' '.join([p.text for p in doc.paragraphs])
        
        # Also check textboxes
        if doc.element.body is not None:
            for txbx in doc.element.body.iter(qn('w:txbxContent')):
                for p in txbx.iter(qn('w:p')):
                    full_text = ''
                    for r in p.iter(qn('w:r')):
                        for t in r.iter(qn('w:t')):
                            if t.text:
                                full_text += t.text
                    document_text += ' ' + full_text
        
        for field, expected_value in fields_to_check.items():
            if expected_value and expected_value in document_text:
                verified_fields[field] = 'PASS'
            elif expected_value:
                verified_fields[field] = 'FAIL'
            else:
                verified_fields[field] = 'N/A'
        
        # Display results
        for field, status in verified_fields.items():
            status_symbol = '[OK]' if status == 'PASS' else ('[FAIL]' if status == 'FAIL' else '[N/A]')
            print("  {} {}: {}".format(status_symbol, field, status))
        
        all_pass = all(s == 'PASS' or s == 'N/A' for s in verified_fields.values())
        print("  Result: {}".format('SUCCESS' if all_pass else 'FAILURE'))
    
    print("")
    print("=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)

if __name__ == '__main__':
    test_comprehensive_cover_page()
