#!/usr/bin/env python3
"""Test generate_cover_page function directly"""
import sys
import traceback
sys.path.insert(0, 'pattern-formatter/backend')

try:
    from coverpage_generator import generate_cover_page
    
    data = {
        'university': 'Bamenda',
        'documentType': 'Assignment',
        'studentName': 'Test',
        'studentId': '001',
        'courseCode': 'CS',
        'courseTitle': 'Test',
        'institution': 'College',
        'faculty': 'Faculty',
        'department': 'Dept',
        'level': '300',
        'instructor': 'Prof',
        'date': '2025-01-21',
        'title': 'Test Title'
    }
    
    print("Calling generate_cover_page...")
    output_path, error = generate_cover_page(data)
    
    if error:
        print(f"❌ Error: {error}")
    else:
        print(f"✅ SUCCESS: {output_path}")
        
except Exception as e:
    print(f"EXCEPTION: {e}")
    traceback.print_exc()
