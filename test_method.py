#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

processor = DocumentProcessor()

# Test the _should_keep_bullet_list method directly
test_bullet_list = {
    'type': 'bullet_list',
    'items': [
        {'type': 'bullet_list', 'content': 'Short'},
        {'type': 'bullet_list', 'content': 'This is a much longer item that exceeds the thirty word limit that we have established'},
        {'type': 'bullet_list', 'content': 'Another short one'},
        {'type': 'bullet_list', 'content': 'Final one'},
    ]
}

should_keep, converted = processor._should_keep_bullet_list(test_bullet_list)

print("Test: 4 items, one with >30 words")
print(f"Should keep as bullets: {should_keep}")
print(f"Expected: False")
print()

# Check the items
print("Items in list:")
for i, item in enumerate(test_bullet_list['items']):
    content = item['content']
    word_count = len(content.split())
    print(f"  Item {i}: {word_count} words - {content[:50]}")
