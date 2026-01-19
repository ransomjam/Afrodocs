#!/usr/bin/env python
"""Test that intended bold-italic still works"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

test_text = """***This should be bold and italic***

Normal text here.

**This should be bold only**

More text.
"""

processor = DocumentProcessor()
result = processor.process_text(test_text)

# Extract analyzed lines
result_dict = result[0] if isinstance(result, tuple) else result
analyzed_lines = result_dict.get('analyzed', []) if isinstance(result_dict, dict) else result_dict

print("Testing intended formatting:")
print("=" * 80)

for i, line in enumerate(analyzed_lines):
    if isinstance(line, dict):
        line_type = line.get('type', 'unknown')
        content = line.get('content', '')[:50]
        formatting = line.get('formatting', {})
        original_format = line.get('original_format', 'none')
        
        print(f"Line {i}: {line_type}")
        print(f"  Content: {content}")
        print(f"  Formatting: {formatting}")
        print(f"  Original format: {original_format}")
        print()

print("=" * 80)
