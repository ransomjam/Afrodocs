#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

from pattern_formatter_backend import DocumentProcessor

with open('test_formatting.txt', 'r', encoding='utf-8') as f:
    content = f.read()

processor = DocumentProcessor()
analyzed = processor.process_text(content)

sections, metadata = analyzed

print(f'Sections type: {type(sections)}')
print(f'Sections keys: {list(sections.keys())}')
print()

for key in sections.keys():
    section = sections[key]
    print(f'{key}:')
    print(f'  Type: {type(section)}')
    if isinstance(section, dict):
        print(f'  Keys: {list(section.keys())[:10]}')
    print()
