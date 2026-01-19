#!/usr/bin/env python
"""Debug what's in the result"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

test_content = """**Rewards**

1. Implications for Students:
"""

processor = DocumentProcessor()
result = processor.process_text(test_content)

print(f"Result type: {type(result)}")
print(f"Result length: {len(result)}")

if isinstance(result, tuple):
    for i, item in enumerate(result):
        print(f"\nItem {i}: {type(item)}")
        if isinstance(item, list):
            print(f"  List length: {len(item)}")
            for j, subitem in enumerate(item[:3]):
                print(f"    [{j}]: {type(subitem)} - {str(subitem)[:80]}")
        else:
            print(f"  Value: {str(item)[:200]}")
