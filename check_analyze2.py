#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

from pattern_formatter_backend import DocumentProcessor
import json

with open('test_formatting.txt', 'r', encoding='utf-8') as f:
    content = f.read()

processor = DocumentProcessor()
analyzed = processor.process_text(content)

print(f'Type of analyzed: {type(analyzed)}')
print(f'Is tuple: {isinstance(analyzed, tuple)}')

if isinstance(analyzed, tuple):
    print(f'Tuple length: {len(analyzed)}')
    sections, _ = analyzed
    print(f'Sections type: {type(sections)}')
    print(f'Sections length: {len(sections)}')
    
    if sections:
        print(f'\nFirst section keys: {list(sections[0].keys())}')
        print(f'First section heading: {sections[0].get("heading", "NO HEADING KEY")}')
else:
    print(f'Length: {len(analyzed)}')
    if analyzed:
        print(f'First item type: {type(analyzed[0])}')
        if isinstance(analyzed[0], dict):
            print(f'First item keys: {list(analyzed[0].keys())}')
