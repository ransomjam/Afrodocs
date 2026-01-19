#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

# Test the failing case
content = """
# Section

- Short
- This is a much longer item that exceeds the thirty word limit that we have established
- Another short one
- Final one
"""

processor = DocumentProcessor()
result = processor.process_text(content)
sections, _ = result

if isinstance(sections, dict) and 'structured' in sections:
    structured = sections['structured']
    for section in structured:
        if section.get('heading') and 'Section' in section.get('heading', ''):
            content_items = section.get('content', [])
            
            for item in content_items:
                if item.get('type') == 'bullet_list':
                    items = item.get('items', [])
                    print("Bullet list items:")
                    for i, li in enumerate(items):
                        content = li.get('content', '')
                        word_count = len(content.split())
                        has_newline = '\n' in content
                        has_colon = ':' in content
                        
                        print(f"  Item {i}: {word_count} words, newline={has_newline}, colon={has_colon}")
                        print(f"    Text: {content[:70]}")
