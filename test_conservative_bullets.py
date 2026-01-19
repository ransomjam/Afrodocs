#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

# Test case: 3 items (should NOT have bullet_list in structured output)
content = """
# Section A

- Item 1
- Item 2  
- Item 3
"""

processor = DocumentProcessor()
result = processor.process_text(content)
sections, metadata = result

print("="*60)
print("TEST: 3 Items (should convert to paragraphs)")
print("="*60)

if isinstance(sections, dict) and 'structured' in sections:
    structured = sections['structured']
    for section in structured:
        if section.get('heading') and 'Section A' in section.get('heading', ''):
            print(f"Section: {section['heading']}")
            content_items = section.get('content', [])
            print(f"Number of content items: {len(content_items)}")
            
            for i, item in enumerate(content_items):
                item_type = item.get('type')
                if item_type == 'bullet_list':
                    print(f"  FAIL: Found bullet_list with {len(item.get('items', []))} items")
                elif item_type == 'paragraph':
                    text = item.get('text', '')
                    print(f"  [P] Paragraph: {text[:50]}")
            
            # Check result
            has_bullets = any(item.get('type') == 'bullet_list' for item in content_items)
            if not has_bullets:
                print("\nResult: PASS - Items converted to paragraphs (no bullet_list)")
            else:
                print("\nResult: FAIL - Still has bullet_list")

print()
print("="*60)
print("TEST: 4 Short Items (should keep as bullet_list)")
print("="*60)

content2 = """
# Section B

- Quick
- Easy
- Simple
- Fast
"""

result2 = processor.process_text(content2)
sections2, _ = result2

if isinstance(sections2, dict) and 'structured' in sections2:
    structured2 = sections2['structured']
    for section in structured2:
        if section.get('heading') and 'Section B' in section.get('heading', ''):
            print(f"Section: {section['heading']}")
            content_items = section.get('content', [])
            print(f"Number of content items: {len(content_items)}")
            
            for i, item in enumerate(content_items):
                item_type = item.get('type')
                if item_type == 'bullet_list':
                    num_items = len(item.get('items', []))
                    print(f"  [B] bullet_list with {num_items} items")
                elif item_type == 'paragraph':
                    text = item.get('text', '')
                    print(f"  [P] Paragraph: {text[:50]}")
            
            # Check result
            has_bullets = any(item.get('type') == 'bullet_list' for item in content_items)
            if has_bullets:
                print("\nResult: PASS - Has bullet_list (4+ short items)")
            else:
                print("\nResult: FAIL - Should have kept bullet_list")
