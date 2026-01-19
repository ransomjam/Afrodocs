#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

test_cases = [
    ("2 items (too few)", """
# Section

- Item 1
- Item 2
""", False),  # Should NOT have bullets
    
    ("3 items (still too few)", """
# Section

- A
- B
- C
""", False),  # Should NOT have bullets
    
    ("4 items (minimum OK)", """
# Section

- First
- Second
- Third
- Fourth
""", True),  # SHOULD have bullets
    
    ("5 items (more than min)", """
# Section

- One
- Two
- Three
- Four
- Five
""", True),  # SHOULD have bullets
    
    ("4 items with one long (>30 words)", """
# Section

- Short
- Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word Word
- Another short one
- Final one
""", False),  # Should NOT use bullets (one too long)
    
    ("4 items with one having colon", """
# Section

- Item
- Title: Description
- Another
- Final
""", False),  # Should NOT use bullets (one has colon)
    
    ("4 short items (valid bullets)", """
# Section

- Item
- Another
- Third
- Fourth
""", True),  # SHOULD have bullets (valid - 4 short items)
]

processor = DocumentProcessor()

print("="*70)
print("CONSERVATIVE BULLET RENDERING TEST SUITE")
print("="*70)
print()

passed = 0
failed = 0

for test_name, content, should_have_bullets in test_cases:
    try:
        result = processor.process_text(content)
        sections, _ = result
        
        if isinstance(sections, dict) and 'structured' in sections:
            structured = sections['structured']
            
            # Find the section
            for section in structured:
                if section.get('heading') and 'Section' in section.get('heading', ''):
                    content_items = section.get('content', [])
                    has_bullets = any(item.get('type') == 'bullet_list' for item in content_items)
                    
                    if has_bullets == should_have_bullets:
                        print(f"[PASS] {test_name}")
                        if has_bullets:
                            bullet_items = [item for item in content_items if item.get('type') == 'bullet_list']
                            print(f"       Rendered as bullet_list with {len(bullet_items[0].get('items', []))} items")
                        else:
                            para_items = [item for item in content_items if item.get('type') == 'paragraph']
                            print(f"       Rendered as {len(para_items)} paragraphs")
                        passed += 1
                    else:
                        expected = "bullets" if should_have_bullets else "paragraphs"
                        actual = "bullets" if has_bullets else "paragraphs"
                        print(f"[FAIL] {test_name}")
                        print(f"       Expected: {expected}, Got: {actual}")
                        failed += 1
                    print()
                    break
    except Exception as e:
        print(f"[ERROR] {test_name}")
        print(f"        {str(e)}")
        failed += 1
        print()

print("="*70)
print(f"RESULTS: {passed} PASSED, {failed} FAILED")
print("="*70)

if failed == 0:
    print("\nAll tests PASSED! Conservative bullet rendering is working correctly.")
else:
    print(f"\n{failed} test(s) FAILED. Please review the logic.")
