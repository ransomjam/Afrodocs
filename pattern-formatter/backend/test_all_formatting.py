#!/usr/bin/env python3
"""
Comprehensive test for formatting options
"""

import requests
import json
from pathlib import Path
from docx import Document
import sys

def test_formatting(font_size, line_spacing, margin_cm, include_toc=False):
    """Test specific formatting combination"""
    test_file = "test_doc.txt"
    with open(test_file, 'w') as f:
        f.write("Test document for formatting.\n" * 100)
    
    params = {
        'include_toc': 'true' if include_toc else 'false',
        'font_size': str(font_size),
        'line_spacing': str(line_spacing),
        'margin_cm': str(margin_cm)
    }
    
    # Login
    session = requests.Session()
    login_response = session.post(
        "http://localhost:5000/api/auth/login",
        json={'username': 'admin', 'password': 'admin123'}
    )
    
    if login_response.status_code != 200:
        print(f"Login failed")
        return False
    
    # Upload
    with open(test_file, 'rb') as f:
        files = {'file': f}
        response = session.post("http://localhost:5000/upload", files=files, data=params)
    
    if response.status_code != 200:
        print(f"Upload failed: {response.json()}")
        return False
    
    result = response.json()
    job_id = result['job_id']
    
    import time
    time.sleep(1)
    
    # Check document
    doc_file = Path(f"./outputs/{job_id}_formatted.docx")
    if not doc_file.exists():
        print(f"Output file not found")
        return False
    
    doc = Document(str(doc_file))
    
    # Check margins
    actual_margin_cm = doc.sections[0].top_margin.inches * 2.54
    margin_ok = abs(actual_margin_cm - margin_cm) < 0.1
    
    # Check font size
    actual_font_pt = None
    if doc.styles['Normal'].font.size:
        actual_font_pt = doc.styles['Normal'].font.size.pt
    
    font_ok = actual_font_pt == font_size
    
    # Check line spacing
    actual_line_spacing = doc.styles['Normal'].paragraph_format.line_spacing
    spacing_ok = abs(actual_line_spacing - line_spacing) < 0.01
    
    # Check TOC
    has_toc = any("Table of Contents" in para.text for para in doc.paragraphs)
    toc_ok = has_toc == include_toc
    
    all_ok = margin_ok and font_ok and spacing_ok and toc_ok
    
    status = "PASS" if all_ok else "FAIL"
    print(f"  [{status}] Font={font_size}pt (actual: {actual_font_pt}), " +
          f"Spacing={line_spacing} (actual: {actual_line_spacing}), " +
          f"Margin={margin_cm}cm (actual: {actual_margin_cm:.2f}), " +
          f"TOC={include_toc} (found: {has_toc})")
    
    import os
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return all_ok

# Run tests
print("Testing formatting options...\n")

test_cases = [
    (10, 1.0, 0.5, False),  # Smallest values
    (12, 1.5, 2.5, False),  # Defaults
    (14, 2.0, 2.0, True),   # Medium with TOC
    (18, 2.5, 3.0, False),  # Larger
    (24, 3.0, 5.0, True),   # Largest with TOC
]

results = []
for font, spacing, margin, toc in test_cases:
    print(f"Test: Font={font}pt, Spacing={spacing}, Margin={margin}cm, TOC={toc}")
    result = test_formatting(font, spacing, margin, toc)
    results.append(result)

print(f"\n{sum(results)}/{len(results)} tests passed")
sys.exit(0 if all(results) else 1)
