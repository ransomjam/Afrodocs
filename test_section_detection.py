#!/usr/bin/env python3
"""
Quick test to verify the section header detection fix
"""

import re
import sys

# Test cases
test_items = [
    "1. Implications for Students:",
    "2. Implications for Teachers",
    "3. Implications for Policy Makers:",
    "a. Enhanced Learning Environment",
    "b. Increased Student Engagement",
    "c. Positive Role Models",
    "I. Introduction",
    "II. Background",
    "1. This is a normal list item with more content",
    "a. Simple subsection",
    "1.1 Hierarchical item",
]

print("=" * 80)
print("SECTION HEADER DETECTION TEST")
print("=" * 80)

for item in test_items:
    trimmed = item.strip()
    print(f"\nItem: {item}")
    
    # Test numeric section (UPDATED PATTERN)
    numeric_section = re.match(r'^\s*(\d+[\.)])\s+(.+?)\s*:?\s*$', trimmed)
    if numeric_section:
        number = numeric_section.group(1)
        title = numeric_section.group(2).strip()
        if title and title[0].isupper() and len(title.split()) <= 8:
            print(f"  -> MATCHED: numeric_section")
            print(f"     Number: {number}")
            print(f"     Title: {title}")
            continue
    
    # Test lettered section (UPDATED PATTERN)
    letter_section = re.match(r'^\s*([a-z][\.)]\s+)(.+?)\s*:?\s*$', trimmed)
    if letter_section:
        letter_prefix = letter_section.group(1)
        title = letter_section.group(2).strip()
        if title and title[0].isupper() and len(title.split()) <= 8:
            print(f"  -> MATCHED: letter_section")
            print(f"     Prefix: {letter_prefix}")
            print(f"     Title: {title}")
            continue
    
    # Test Roman section (UPDATED PATTERN)
    roman_section = re.match(r'^\s*([IVX]+[\.)])\s+(.+?)\s*:?\s*$', trimmed, re.IGNORECASE)
    if roman_section:
        number = roman_section.group(1)
        title = roman_section.group(2).strip()
        if title and title[0].isupper() and len(title.split()) <= 8:
            print(f"  -> MATCHED: roman_section")
            print(f"     Number: {number}")
            print(f"     Title: {title}")
            continue
    
    print(f"  -> NO MATCH - would be classified differently")

print("\n" + "=" * 80)
print("ANALYSIS")
print("=" * 80)
print("""
Expected Results:
- "1. Implications..." -> numeric_section (shortdoc_header)
- "2. Implications..." -> numeric_section (shortdoc_header)
- "3. Implications..." -> numeric_section (shortdoc_header)
- "a. Enhanced..." -> letter_section (shortdoc_subheader)
- "b. Increased..." -> letter_section (shortdoc_subheader)
- "c. Positive..." -> letter_section (shortdoc_subheader)
- "I. Introduction" -> roman_section (shortdoc_header)
- "1. normal list..." -> NO MATCH - numbered_list (actual list item)
""")

