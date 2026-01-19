#!/usr/bin/env python3
"""
Test fix for double-numbering issue
Verify that items with existing numbering don't get double-numbered
"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

# Sample content with existing numbering that should NOT be double-numbered
test_content = """
CHAPTER ONE: INTRODUCTION

1. Implications for Students:

This section discusses implications for students.

1.1 Enhanced Learning Environment

When teachers are motivated, they create better environments.

1.2 Increased Student Engagement

Motivated teachers employ innovative teaching methods.

1. Job Satisfaction

Teachers with motivation experience job satisfaction.

1.2 Professional Growth

Motivated teachers engage in continuous professional development.

I. Implications for Teachers:

Important implications for the teaching profession.

I.1 Enhanced Job Satisfaction

Teachers experience higher job satisfaction.

II. Career Development:

Career development opportunities emerge.

II.1 Professional Opportunities

New opportunities for growth.
"""

# Process the text
processor = DocumentProcessor()
print("Processing document with existing numbering...")
print("=" * 70)

# This would normally be called through the API, but we're testing directly
lines = test_content.strip().split('\n')

# Parse and structure
structured = processor.structure_document(test_content)

print(f"\nParsed structure:")
print(f"Total sections: {len(structured.get('sections', []))}")

# Check the sections for double numbering
for section in structured.get('sections', [])[:10]:
    if 'title' in section:
        print(f"\nSection: {section.get('title')}")
        print(f"  Type: {section.get('type')}")
        if section.get('type') == 'numbered_list':
            items = section.get('items', [])
            print(f"  Items count: {len(items)}")
            for i, item in enumerate(items[:3]):
                if isinstance(item, dict):
                    print(f"    Item {i+1}: {item.get('content', '')[:60]}")
                else:
                    print(f"    Item {i+1}: {str(item)[:60]}")

print("\n" + "=" * 70)
print("Test complete. Check for double numbering patterns like:")
print("  - '1. I. Something' (should be '1. Something' or 'I. Something')")
print("  - '1. 1.1 Something' (should be '1.1 Something')")
