#!/usr/bin/env python
"""Debug indentation and section break detection"""

import sys
import re
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

test_content = """a. Improved academic performance through better resource allocation
b. Enhanced engagement with course materials
c. Stronger connections with peer support networks
d. Better understanding of personal learning styles

---

2. Institutional Benefits:"""

print("Analyzing each line:")
for i, line in enumerate(test_content.split('\n')):
    print(f"\nLine {i}: {repr(line)}")
    print(f"  Length: {len(line)}")
    print(f"  Leading spaces: {len(line) - len(line.lstrip())}")
    
    # Test each pattern
    if re.match(r'^\s{2,}[a-zA-Z0-9]\.\s+', line):
        print(f"  ✓ Matches INDENT_ITEM pattern")
    
    if re.match(r'^\d+\.\s+[A-Z]', line):
        print(f"  ✓ Matches NUMBERED_HEADER pattern")
    
    stripped = line.strip()
    if re.match(r'^-{3,}$', stripped):
        print(f"  ✓ Matches SECTION_BREAK pattern (dashes)")
    
    if re.match(r'^\*{3,}$', stripped):
        print(f"  ✓ Matches SECTION_BREAK pattern (asterisks)")
