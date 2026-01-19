#!/usr/bin/env python3
"""
Test the new institutions (BUST and Catholic University)
"""

import sys
import json
import os
from pathlib import Path

# Add backend to path
backend_path = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\backend"
sys.path.insert(0, backend_path)

from coverpage_generator import generate_cover_page
from docx import Document

def test_institution(institution_id, institution_name, document_type="Assignment"):
    """Test generating a cover page for an institution"""
    
    print(f"\n{'='*80}")
    print(f"Testing: {institution_name} ({institution_id})")
    print(f"Document Type: {document_type}")
    print(f"{'='*80}")
    
    try:
        # Create test data
        student_data = {
            'institution': institution_id,
            'studentName': 'Test Student',
            'studentId': 'TEST001',
            'supervisorName': 'Test Supervisor',
            'department': 'Test Department',
            'courseCode': 'TEST101',
            'courseTitle': 'Test Course',
            'year': '2024',
            'documentType': document_type,
            'title': 'Test Cover Page'
        }
        
        # Generate document
        output_path, error = generate_cover_page(student_data)
        
        if error:
            print(f"❌ Error generating document: {error}")
            return False, 0
        
        if output_path and os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"✅ Document generated successfully")
            print(f"   Output path: {output_path}")
            print(f"   File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            
            # Verify it's a valid DOCX
            try:
                doc = Document(output_path)
                print(f"   Valid DOCX: ✅ (contains {len(doc.paragraphs)} paragraphs)")
                return True, file_size
            except Exception as e:
                print(f"   ❌ Invalid DOCX: {e}")
                return False, 0
        else:
            print(f"❌ Document not created at {output_path}")
            return False, 0
            
    except Exception as e:
        print(f"❌ Error generating document: {e}")
        import traceback
        traceback.print_exc()
        return False, 0

print("Testing New Institutions Implementation")
print("="*80)

# Test BUST with different document types
print("\n[TEST] BUST (Bamenda University of Science and Technology)")
bust_results = {}
for doc_type in ["Assignment", "Thesis", "Research Proposal", "Internship Report"]:
    success, size = test_institution("bust", "BUST", doc_type)
    bust_results[doc_type] = (success, size)

# Test Catholic University with different document types
print("\n\n[TEST] CUCB (The Catholic University of Cameroon, Bamenda)")
cucb_results = {}
for doc_type in ["Assignment", "Thesis", "Research Proposal", "Internship Report"]:
    success, size = test_institution("cucb", "CUCB", doc_type)
    cucb_results[doc_type] = (success, size)

# Summary
print("\n" + "="*80)
print("TEST SUMMARY")
print("="*80)

print("\n[RESULTS] BUST:")
bust_success = sum(1 for s, _ in bust_results.values() if s)
print(f"  Passed: {bust_success}/{len(bust_results)}")
for doc_type, (success, size) in bust_results.items():
    status = "[OK]" if success else "[FAIL]"
    print(f"    {status} {doc_type:20s} - {size:8,} bytes")

print("\n[RESULTS] CUCB:")
cucb_success = sum(1 for s, _ in cucb_results.values() if s)
print(f"  Passed: {cucb_success}/{len(cucb_results)}")
for doc_type, (success, size) in cucb_results.items():
    status = "[OK]" if success else "[FAIL]"
    print(f"    {status} {doc_type:20s} - {size:8,} bytes")

# Verify template differences (file sizes should differ from Bamenda)
print("\n[VERIFICATION] FILE SIZE VERIFICATION")
print("  (Should differ from Bamenda templates to confirm different templates are used)")

# Get a Bamenda file size for comparison
bamenda_success, bamenda_size = test_institution("uba", "Bamenda", "Assignment")
print(f"\n  Reference (Bamenda Assignment): {bamenda_size:,} bytes")

all_bust_sizes = [size for _, size in bust_results.values()]
if all_bust_sizes:
    print(f"  BUST Assignment: {all_bust_sizes[0]:,} bytes")
    if all_bust_sizes[0] != bamenda_size:
        print(f"    [OK] Different from Bamenda (correct - uses own templates)")
    else:
        print(f"    [WARN] Same as Bamenda (may indicate template issue)")

all_cucb_sizes = [size for _, size in cucb_results.values()]
if all_cucb_sizes:
    print(f"  CUCB Assignment: {all_cucb_sizes[0]:,} bytes")
    if all_cucb_sizes[0] != bamenda_size:
        print(f"    [OK] Different from Bamenda (correct - uses own templates)")
    else:
        print(f"    [WARN] Same as Bamenda (may indicate template issue)")

# Overall result
total_tests = len(bust_results) + len(cucb_results) + 1
total_passed = bust_success + cucb_success + (1 if bamenda_success else 0)

print(f"\n{'='*80}")
print(f"OVERALL: {total_passed}/{total_tests} tests passed")
if total_passed == total_tests:
    print("[SUCCESS] ALL TESTS PASSED - Implementation complete!")
else:
    print(f"[WARNING] {total_tests - total_passed} tests failed - Review errors above")
print(f"{'='*80}")
