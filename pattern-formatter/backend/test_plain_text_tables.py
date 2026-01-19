#!/usr/bin/env python3
"""
Test script for plain text table detection and rendering
"""

import sys
import os
import tempfile

# Add current directory to path
sys.path.insert(0, os.getcwd())

from pattern_formatter_backend import PatternEngine, WordGenerator

def test_plain_text_table():
    """Test plain text table detection and Word document generation"""

    # Sample plain text table content
    test_content = """
Here is some text before the table.

Variable    Mean    SD      N
Age         25.3    4.2     150
Income      45000   12000   150
Education   14.2    2.1     150

This is text after the table.

Another table:

| Name | Value | Unit |
|------|-------|------|
| Temp | 23.5  | °C   |
| Pres | 1013  | hPa  |

And some more text.
"""

    print("Testing plain text table detection...")

    # Initialize PatternEngine
    engine = PatternEngine()

    # Analyze the content
    sections = engine.analyze(test_content)

    print(f"Found {len(sections)} sections:")
    for i, section in enumerate(sections):
        print(f"  Section {i}: type={section.get('type')}, content_length={len(section.get('content', []))}")

    # Create Word document
    generator = WordGenerator()

    # Generate document
    doc_path = os.path.join(tempfile.gettempdir(), "test_plain_text_tables.docx")
    generator.generate_document(sections, doc_path)

    print(f"Document generated at: {doc_path}")
    print("Test completed successfully!")

if __name__ == "__main__":
    test_plain_text_table()