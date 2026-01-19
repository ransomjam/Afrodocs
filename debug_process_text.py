#!/usr/bin/env python
"""Debug process_text output"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

test_content = """**Rewards**

1. Implications for Students:

a. First item
b. Second item

---

2. Institutional Benefits:"""

processor = DocumentProcessor()
analyzed_lines, images = processor.process_text(test_content)

print(f"Total lines: {len(analyzed_lines)}")
print("\nAnalyzed lines:")
for i, line in enumerate(analyzed_lines):
    if isinstance(line, dict):
        line_type = line.get('type', 'unknown')
        content = str(line.get('content', ''))[:50]
        print(f"  {i+1}. [{line_type}] {content}")
    else:
        print(f"  {i+1}. [non-dict] {str(line)[:50]}")
