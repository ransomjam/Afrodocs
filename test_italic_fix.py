#!/usr/bin/env python
"""Test that unwanted italics are removed"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

test_text = """**Key Topics**

1. Introduction

This is body text with some content that should not be italicized.

2. Methodology

The study examined various parameters and collected data systematically.

**Important Findings**

Results showed significant improvements across all measured dimensions.
"""

processor = DocumentProcessor()
result = processor.process_text(test_text)

# Extract analyzed lines
result_dict = result[0] if isinstance(result, tuple) else result
analyzed_lines = result_dict.get('analyzed', []) if isinstance(result_dict, dict) else result_dict

print("Analysis results:")
print("=" * 80)

for i, line in enumerate(analyzed_lines):
    if isinstance(line, dict):
        line_type = line.get('type', 'unknown')
        content = line.get('content', '')[:50]
        formatting = line.get('formatting', {})
        
        # Check for italic formatting
        has_italic = formatting.get('italic', False)
        
        if has_italic:
            print(f"[WARNING] Line {i}: ITALICIZED - {line_type}")
            print(f"  Content: {content}")
            print(f"  Formatting: {formatting}")
        elif line_type in ['shortdoc_header', 'prominent_heading']:
            print(f"[OK] Line {i}: {line_type} - {content}")
        elif line_type == 'paragraph':
            print(f"[OK] Line {i}: {line_type} - {content}")

print("\n" + "=" * 80)
print("Test complete - check for any WARNING lines with italics")
