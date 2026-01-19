#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Quick test of bullet limiting logic
"""

import sys
sys.path.insert(0, 'pattern-formatter/backend')

# Import directly without running the server
import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

# Simple inline test
content = """
# Section A (3 items - should NOT use bullets)

- Item 1
- Item 2  
- Item 3

# Section B (4 short items - should use bullets)

- Quick
- Easy
- Fast
- Simple

# Section C (4 items with one having colon - should NOT use bullets)

- Item: Description
- Item 2
- Item 3
- Item 4
"""

processor = DocumentProcessor()
sections, _ = processor.process_text(content)

print("Analyzing sections...")
print()

for section_key, section_data in sections.items():
    heading = section_data.get('heading', 'Unknown')
    content_items = section_data.get('content', [])
    
    print(f"Section: {heading}")
    
    for item in content_items:
        item_type = item.get('type')
        
        if item_type == 'bullet_list':
            items = item.get('items', [])
            print(f"  ✓ Has bullet_list with {len(items)} items")
            for i, li in enumerate(items[:3]):
                text = li if isinstance(li, str) else li.get('content', '')
                print(f"    - {text[:50]}")
        elif item_type == 'paragraph':
            text = item.get('text', '')
            if text:
                print(f"  - Paragraph: {text[:50]}")
    
    print()

print("="*60)
print("Expected Results:")
print("  Section A (3 items): Should NOT have bullet_list")
print("  Section B (4 short): Should have bullet_list")
print("  Section C (with colon): Should NOT have bullet_list")
