#!/usr/bin/env python
"""Debug classification of asterisk-wrapped items"""

import sys
import re
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor, PatternEngine

# Create engine directly to test classification
engine = PatternEngine()

test_lines = [
    "**1. Implications for Students:**",
    "1. Implications for Students:",
    "***Enhanced Learning Outcomes***",
    "Enhanced Learning Outcomes",
]

print("Testing classification directly:")
print("=" * 80)

for line in test_lines:
    # Strip asterisks for comparison
    stripped = line.replace('**', '').replace('***', '').replace('*', '')
    
    # Classify
    analysis = engine.analyze_line(line, 0, '', '')
    
    print(f"Input:  {line}")
    print(f"Stripped: {stripped}")
    print(f"  Type: {analysis.get('type')}")
    print(f"  Content: {analysis.get('content')}")
    print()
