#!/usr/bin/env python
"""Debug what TextFormatterWithRegex does"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import TextFormatterWithRegex

formatter = TextFormatterWithRegex()

test_texts = [
    "**1. Implications for Students:**",
    "***Enhanced Learning Outcomes***",
    "*Student Engagement*",
    "1. Implications for Students:",
]

print("TextFormatterWithRegex output:")
print("=" * 80)

for text in test_texts:
    formatted = formatter.format_text(text)
    print(f"Input:  {text}")
    print(f"Output: {formatted}")
    print()
