#!/usr/bin/env python3
"""Test that page breaks are removed when processing AI-pasted text"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pattern_formatter_backend import DocumentProcessor
from docx import Document
from docx.oxml.ns import qn

SAMPLE_TEXT = """## 1. History of Artificial Intelligence

The field of artificial intelligence began in the 1950s.

---

## 2. Modern Applications

Today AI is used in many fields.

---

## 3. Future Prospects

The future of AI is bright.
"""

def count_page_breaks(doc_path):
    """Count page breaks in a Word document"""
    doc = Document(doc_path)
    count = 0
    locations = []
    
    for i, para in enumerate(doc.paragraphs):
        para_text = para.text[:40] if para.text else '[empty]'
        
        # Check for w:br elements with type="page"
        for elem in para._element.iter():
            if elem.tag == qn('w:br'):
                br_type = elem.get(qn('w:type'))
                if br_type == 'page':
                    count += 1
                    locations.append(f"Para {i}: '{para_text}'")
    
    return count, locations

def main():
    print("=" * 60)
    print("PAGE BREAK FIX TEST")
    print("=" * 60)
    
    output_path = os.path.join(os.path.dirname(__file__), 'outputs', 'test_page_break_final.docx')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"\nProcessing sample text with --- markers...")
    processor = DocumentProcessor()
    result_dict, images = processor.process_text(SAMPLE_TEXT)
    
    # Extract structured data from result dict
    structured = result_dict.get('structured', [])
    
    print(f"\nStructured into {len(structured)} sections")
    
    # Check sections for page break flags
    for i, section in enumerate(structured):
        heading = section.get('title', section.get('heading', 'N/A'))[:30]
        npb = section.get('needs_page_break', False)
        sonp = section.get('start_on_new_page', False)
        print(f"  [{i}] '{heading}' needs_page_break={npb}, start_on_new_page={sonp}")
    
    # Quick check: long dash normalization
    print('\nVerifying dash normalization in cleaned lines:')
    any_replaced = False
    for a in result.get('analyzed', []):
        text = a.get('text', '')
        if '\u2014' in text or '\u2013' in text or '--' in text:
            print('  WARN: dash still present in analyzed line:', text)
        if ', ' in text and ('—' in text or '–' in text or '--' in text):
            any_replaced = True

    if any_replaced:
        print('  ✓ Some dashes were normalized to comma+space in analyzed text')

    # Use WordGenerator to create document
    from pattern_formatter_backend import WordGenerator
    generator = WordGenerator()
    
    # Generate document
    generator.generate(structured, output_path, images=[])
    result = output_path
    
    print(f"\nGenerated: {result}")
    print(f"Generator is_short_document: {generator.is_short_document}")
    
    # Count page breaks
    count, locations = count_page_breaks(result)
    
    print(f"\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Page breaks found: {count}")
    
    if locations:
        print("\nPage break locations:")
        for loc in locations:
            print(f"  - {loc}")
    
    if count == 0:
        print("\n✓ SUCCESS: No page breaks in output document!")
        print("  The fix for AI-pasted text with --- markers is working correctly.")
    else:
        print(f"\n✗ FAILURE: Found {count} page breaks!")
        print("  Further investigation needed.")
    
    return count

if __name__ == '__main__':
    exit(main())
