#!/usr/bin/env python3
"""
Verify that all headings in the generated DOCX file use Times New Roman font.
This checks both the style definitions and the actual run formatting.
"""

from docx import Document
from pathlib import Path
import sys

def check_document_fonts(docx_path):
    """Check all headings in a DOCX document for font consistency"""
    doc = Document(docx_path)
    
    issues = []
    heading_count = 0
    
    print(f"\n{'='*80}")
    print(f"Checking: {Path(docx_path).name}")
    print(f"{'='*80}\n")
    
    # Check heading styles
    print("CHECKING HEADING STYLES:")
    print("-" * 80)
    for style_name in ['Heading 1', 'Heading 2', 'Heading 3', 'Title']:
        try:
            style = doc.styles[style_name]
            style_font_name = style.font.name
            print(f"  {style_name:15} -> Font: {style_font_name}")
            if style_font_name != 'Times New Roman':
                issues.append(f"Style {style_name} uses {style_font_name}, not Times New Roman")
        except KeyError:
            pass
    
    # Check all paragraphs for heading styles
    print("\nCHECKING HEADING PARAGRAPHS:")
    print("-" * 80)
    
    for i, para in enumerate(doc.paragraphs):
        # Check if it's a heading (by style)
        if para.style.name.startswith('Heading') or para.style.name in ['Title', 'Title 1']:
            heading_count += 1
            heading_text = para.text.strip()[:60]  # First 60 chars
            
            # Check each run in the paragraph
            all_tnr = True
            fonts_found = set()
            
            if para.runs:
                for run in para.runs:
                    if run.font.name:
                        fonts_found.add(run.font.name)
                        if run.font.name != 'Times New Roman':
                            all_tnr = False
            
            status = "✓" if all_tnr else "✗"
            font_info = f"Fonts: {', '.join(fonts_found) if fonts_found else 'NONE SET (using style)'}"
            
            print(f"{status} [{para.style.name:12}] {heading_text:60} | {font_info}")
            
            if not all_tnr and fonts_found:
                issues.append(f"Heading '{heading_text}' uses {fonts_found}, not Times New Roman")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: Found {heading_count} headings in document")
    print(f"{'='*80}")
    
    if issues:
        print(f"\n❌ FONT ISSUES FOUND ({len(issues)}):")
        for issue in issues:
            print(f"  • {issue}")
        return False
    else:
        print(f"\n✅ ALL HEADINGS USE TIMES NEW ROMAN!")
        return True

if __name__ == '__main__':
    # Get the most recent DOCX file
    outputs_dir = Path(r'C:\Users\user\Desktop\PATTERN\pattern-formatter\backend\outputs')
    
    docx_files = sorted(outputs_dir.glob('*.docx'), key=lambda x: x.stat().st_mtime, reverse=True)
    
    if not docx_files:
        print("❌ No DOCX files found in outputs directory")
        sys.exit(1)
    
    latest_file = docx_files[0]
    print(f"Testing latest file: {latest_file.name}")
    
    success = check_document_fonts(str(latest_file))
    sys.exit(0 if success else 1)
