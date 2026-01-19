#!/usr/bin/env python
"""Test main heading formatting in dissertations"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

def check_heading_formatting(docx_path):
    """Check how main headings are formatted"""
    doc = Document(docx_path)
    
    print(f"\n{'='*80}")
    print(f"Analyzing: {os.path.basename(docx_path)}")
    print(f"{'='*80}\n")
    
    main_headings = ['RESUME', 'LITERATURE REVIEW', 'ABSTRACT', 'ACKNOWLEDGEMENTS', 
                     'INTRODUCTION', 'METHODOLOGY']
    
    for i, para in enumerate(doc.paragraphs[:100]):  # Check first 100 paragraphs
        text = para.text.strip().upper()
        
        # Check if this is a main heading
        is_main_heading = any(heading in text for heading in main_headings)
        
        if is_main_heading or para.style.name.startswith('Heading'):
            print(f"Para {i}: {para.text[:60]}")
            print(f"  Style: {para.style.name}")
            print(f"  Alignment: {para.alignment}")
            print(f"  Expected alignment (CENTER): {WD_ALIGN_PARAGRAPH.CENTER}")
            
            # Check run formatting
            for run in para.runs:
                print(f"    Run: {run.text[:40]}")
                print(f"      Bold: {run.bold}")
                print(f"      Font: {run.font.name}")
                print(f"      Size: {run.font.size}")
                print(f"      Color: {run.font.color.rgb}")
            print()

if __name__ == '__main__':
    # Test with dissertation
    test_file = r'c:\Users\user\Desktop\PATTERN\Samples\sample_dissertation.docx'
    if os.path.exists(test_file):
        check_heading_formatting(test_file)
    else:
        print(f"File not found: {test_file}")
        
    # Also test by processing and exporting
    print("\n" + "="*80)
    print("Testing RESUME formatting...")
    print("="*80 + "\n")
    
    processor = DocumentProcessor()
    output_path = r'c:\Users\user\Desktop\PATTERN\test_resume_output.docx'
    result = processor.process_docx(test_file)
    
    # Check the output
    if result:
        check_heading_formatting(output_path)
