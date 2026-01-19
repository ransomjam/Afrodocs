#!/usr/bin/env python
"""Test that text within asterisks is bolded"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

test_text = """**1. Implications for Students:**

***Enhanced Learning Outcomes***

*Student Engagement*

Normal text without formatting.
"""

processor = DocumentProcessor()
result = processor.process_text(test_text)

# Extract analyzed lines
result_dict = result[0] if isinstance(result, tuple) else result
analyzed_lines = result_dict.get('analyzed', []) if isinstance(result_dict, dict) else result_dict

print("Testing asterisk formatting:")
print("=" * 80)

for i, line in enumerate(analyzed_lines):
    if isinstance(line, dict):
        line_type = line.get('type', 'unknown')
        content = line.get('content', '')
        formatting = line.get('formatting', {})
        
        print(f"Line {i}: {line_type}")
        print(f"  Content: {content}")
        print(f"  Formatting: {formatting}")
        
        # Check if should be bold
        if '*' in content or formatting.get('bold'):
            print(f"  -> BOLD: YES")
        else:
            print(f"  -> BOLD: NO")
        print()

print("=" * 80)
