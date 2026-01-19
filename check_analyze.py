#!/usr/bin/env python

import sys
sys.path.insert(0, 'pattern-formatter/backend')

from pattern_formatter_backend import DocumentProcessor
import json

with open('test_formatting.txt', 'r') as f:
    content = f.read()

processor = DocumentProcessor()
analyzed = processor.process_text(content)

print(f'Type of analyzed: {type(analyzed)}')
print(f'Length: {len(analyzed)}')
print()

# Print first item
if analyzed:
    print('First item:')
    first = analyzed[0]
    print(f'Type: {type(first)}')
    print(f'Keys/Content: {first}')
    print()
    
# Print all items
print('All items:')
for i, item in enumerate(analyzed):
    print(f'{i}: {item}')
