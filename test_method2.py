#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

processor = DocumentProcessor()

# Test with an actually long sentence
long_sentence = " ".join(["word"] * 35)  # 35 words

test_bullet_list = {
    'type': 'bullet_list',
    'items': [
        {'type': 'bullet_list', 'content': 'Short'},
        {'type': 'bullet_list', 'content': long_sentence},
        {'type': 'bullet_list', 'content': 'Another'},
        {'type': 'bullet_list', 'content': 'Final'},
    ]
}

should_keep, converted = processor._should_keep_bullet_list(test_bullet_list)

print("Test: 4 items, one with 35 words")
print(f"Should keep as bullets: {should_keep}")
print(f"Expected: False")
print(f"Result: {'PASS' if not should_keep else 'FAIL'}")
print()

# Check the items
print("Items in list:")
for i, item in enumerate(test_bullet_list['items']):
    content = item['content']
    word_count = len(content.split())
    print(f"  Item {i}: {word_count} words")
