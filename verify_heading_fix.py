#!/usr/bin/env python
"""Verify main heading formatting after fix"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
import shutil

def check_heading_formatting(docx_path):
    """Check how main headings are formatted"""
    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        return False
    
    doc = Document(docx_path)
    
    print(f"\n{'='*80}")
    print(f"Analyzing: {os.path.basename(docx_path)}")
    print(f"{'='*80}\n")
    
    main_headings = ['RESUME', 'LITERATURE REVIEW', 'ABSTRACT', 'ACKNOWLEDGEMENTS', 
                     'INTRODUCTION', 'METHODOLOGY', 'DECLARATION', 'CERTIFICATION']
    
    found_main_headings = False
    all_correct = True
    
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip().upper()
        
        # Check if this is a main heading
        is_main_heading = any(heading in text for heading in main_headings)
        
        if is_main_heading or para.style.name.startswith('Heading'):
            found_main_headings = True
            is_center = para.alignment == WD_ALIGN_PARAGRAPH.CENTER
            
            print(f"Para {i}: {para.text[:60]}")
            print(f"  Style: {para.style.name}")
            print(f"  Alignment: {para.alignment} {'✓ CENTER' if is_center else '✗ NOT CENTER'}")
            
            # Check run formatting
            all_bold = all(run.bold for run in para.runs)
            all_times = all(run.font.name == 'Times New Roman' for run in para.runs)
            all_sized = all(run.font.size is not None for run in para.runs)
            all_black = all(str(run.font.color.rgb) == '000000' for run in para.runs if run.font.color.rgb)
            
            print(f"  Formatting:")
            print(f"    Bold: {all_bold} {'✓' if all_bold else '✗'}")
            print(f"    Font Name (Times New Roman): {all_times} {'✓' if all_times else '✗'}")
            print(f"    Font Size: {all_sized} {'✓' if all_sized else '✗'}")
            print(f"    Color (Black): {all_black} {'✓' if all_black else '✗'}")
            
            if not (is_center and all_bold and all_times and all_sized):
                all_correct = False
                print(f"  ⚠️  ISSUE FOUND!")
            else:
                print(f"  ✓ Correctly formatted")
            print()
    
    if not found_main_headings:
        print("No main headings found (might be OK for short docs)")
    
    return all_correct

if __name__ == '__main__':
    # Check the uploaded file
    output_dir = r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend\uploads'
    
    # Find the most recently created file
    if os.path.exists(output_dir):
        files = [(f, os.path.getmtime(os.path.join(output_dir, f))) 
                 for f in os.listdir(output_dir) if f.endswith('.docx')]
        if files:
            latest_file = max(files, key=lambda x: x[1])[0]
            latest_path = os.path.join(output_dir, latest_file)
            
            print(f"Checking latest uploaded file: {latest_file}")
            result = check_heading_formatting(latest_path)
            
            if result:
                print("\n" + "="*80)
                print("✓ All main headings are correctly formatted!")
                print("="*80)
            else:
                print("\n" + "="*80)
                print("⚠️  Some formatting issues found")
                print("="*80)
