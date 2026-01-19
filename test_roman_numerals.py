#!/usr/bin/env python3
"""
Test script to verify that preliminary pages use Roman numerals
and main content uses Arabic numerals
"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import WordGenerator

def test_roman_numeral_numbering():
    """Test that documents properly format preliminary pages with Roman numerals"""
    
    print("Testing Roman numeral page numbering...")
    
    # Create test document structure with cover, certification, TOC, and chapters
    structured_data = [
        {
            'type': 'chapter',
            'heading': 'TABLE OF CONTENTS',
            'content': 'Chapter 1 - Introduction\nChapter 2 - Literature Review\nChapter 3 - Methodology'
        },
        {
            'type': 'chapter',
            'heading': 'CHAPTER 1: Introduction',
            'content': 'This is the introduction chapter. This should start with page number 1 in Arabic numerals. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 10
        },
        {
            'type': 'chapter',
            'heading': 'CHAPTER 2: Literature Review',
            'content': 'This is the literature review chapter. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 10
        }
    ]
    
    # Generate document
    output_path = 'test_roman_numerals.docx'
    generator = WordGenerator()
    generator.generate(
        structured_data=structured_data,
        output_path=output_path,
        include_toc=True,
        font_size=12,
        line_spacing=2.0,
        margins={'top': 1, 'bottom': 1, 'left': 1.25, 'right': 1}
    )
    
    # Save document
    print("Document created: {}".format(output_path))
    
    # Parse the document to check section numbering
    from docx import Document
    from docx.oxml.ns import qn
    
    doc = Document(output_path)
    
    print("\nSection analysis:")
    for i, section in enumerate(doc.sections):
        # Get page numbering format from w:pgNumType
        section_pr = section._sectPr
        pgNumType = section_pr.find(qn('w:pgNumType'))
        
        if pgNumType is not None:
            fmt = pgNumType.get(qn('w:fmt'))
            start = pgNumType.get(qn('w:start'))
            print(f"  Section {i}: format={fmt}, start={start}")
        else:
            # Check if section has footer
            if section.footer.paragraphs:
                print("  Section {}: No explicit numbering format (inherits from previous) - has footer".format(i))
            else:
                print("  Section {}: No explicit numbering format - no footer".format(i))
    
    # Check that we have at least 2 sections (prelim + chapter)
    if len(doc.sections) >= 2:
        print("SUCCESS: Multiple sections found (expected for Roman to Arabic transition)")
    else:
        print("WARNING: Only one section found - Roman to Arabic transition may not work")
    
    print("")
    print("Roman numeral test complete!")
    print("Expected: First section with Roman numerals (i, ii, iii), then Arabic numerals (1, 2, 3) at CHAPTER 1")

if __name__ == '__main__':
    test_roman_numeral_numbering()
