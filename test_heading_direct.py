#!/usr/bin/env python
"""Direct test of heading formatting fix"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Process the dissertation directly
processor = DocumentProcessor()
test_file = r'c:\Users\user\Desktop\PATTERN\Samples\sample_dissertation.docx'
output_file = r'c:\Users\user\Desktop\PATTERN\test_heading_output.docx'

# Process it
result = processor.process_docx(test_file)
if result:
    processor.doc.save(output_file)
else:
    print("Failed to process document")
    sys.exit(1)

# Now check the output
doc = Document(output_file)

print("\n" + "="*80)
print("Checking Main Heading Formatting")
print("="*80 + "\n")

main_headings = ['RESUME', 'LITERATURE REVIEW', 'ABSTRACT', 'ACKNOWLEDGEMENTS', 
                 'INTRODUCTION', 'METHODOLOGY', 'DECLARATION', 'CERTIFICATION']

found_headings = 0
correct_headings = 0

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip().upper()
    
    # Check if this is a main heading
    is_main = any(h in text for h in main_headings)
    
    if is_main or para.style.name.startswith('Heading'):
        found_headings += 1
        
        # Check all formatting requirements
        is_center = para.alignment == WD_ALIGN_PARAGRAPH.CENTER
        is_heading_style = para.style.name.startswith('Heading')
        all_bold = all(run.bold for run in para.runs) if para.runs else False
        all_times = all(run.font.name == 'Times New Roman' for run in para.runs) if para.runs else False
        
        is_correct = is_heading_style and (is_center or not is_main) and all_bold
        
        if is_correct:
            correct_headings += 1
            marker = "✓"
        else:
            marker = "✗"
        
        print(f"{marker} Para {i}: {text[:60]}")
        print(f"  Style: {para.style.name}")
        print(f"  Heading Style: {is_heading_style}")
        print(f"  Bold: {all_bold}")
        print(f"  Times NR: {all_times}")
        if is_main:
            print(f"  Centered: {is_center}")
        print()

print("="*80)
print(f"Summary: {correct_headings}/{found_headings} headings correctly formatted")
if correct_headings == found_headings and found_headings > 0:
    print("✓ All main headings are properly formatted!")
else:
    print("⚠️  Some formatting issues found")
print("="*80)
