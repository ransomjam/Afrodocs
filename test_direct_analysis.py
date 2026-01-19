#!/usr/bin/env python3
"""Direct test of PatternEngine analysis"""

import sys
import os
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')
os.environ['FLASK_ENV'] = 'production'

from pattern_formatter_backend import PatternEngine

text = """1. Implications for Students:
Students face challenges.

1. Financial Considerations:
Managing finances is crucial.

1. Mental Health Support:
Universities need resources.

2. Recommendations:
Following recommendations.

2. Policy Changes:
New policies needed."""

# Analyze with PatternEngine
engine = PatternEngine()
structured = engine.analyze_text(text)

print('ANALYSIS RESULTS:')
print('=' * 60)
for item in structured:
    if item['type'] == 'numbered_list':
        print(f'\nType: numbered_list')
        for i, list_item in enumerate(item.get('items', []), 1):
            item_str = str(list_item)[:80]
            print(f'  Item {i}: {item_str}')
    else:
        content = str(item.get('content', ''))[:80]
        print(f'\nType: {item["type"]} - {content}')
