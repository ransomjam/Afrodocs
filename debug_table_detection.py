#!/usr/bin/env python3
"""Debug script to trace markdown table detection"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import PatternEngine

test_lines = [
    "| Protocol | Purpose                 | Transport | Common Port(s) |",
    "| -------- | ----------------------- | --------: | -------------: |",
    "| HTTP     | Web browsing            |       TCP |             80 |",
    "| HTTPS    | Secure web              |       TCP |            443 |",
]

engine = PatternEngine()

print("Testing markdown table detection:")
print("=" * 60)

for line in test_lines:
    analysis = engine.analyze_line(line, 0, '', '')
    print(f"\nLine: {line[:60]}")
    print(f"Type: {analysis['type']}")
    if analysis['type'] == 'table':
        print(f"  Subtype: {analysis.get('subtype')}")
        print(f"  Metadata: {analysis.get('metadata')}")
    print(f"  Confidence: {analysis.get('confidence')}")
