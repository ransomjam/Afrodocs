#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test reference formatting"""

import re

def _format_single_apa_reference(text):
    """Apply APA formatting rules to a single reference string."""
    # Fix missing space before year parentheses: "UNESCO(2024)" -> "UNESCO (2024)"
    text = re.sub(r'([^\s\(])\((\d{4})', r'\1 (\2', text)
    
    # Fix capitalization in titles (ensure space after colon)
    text = re.sub(r'([A-Z][a-z]+)\s+([A-Z][a-z]+):', r'\1 \2:', text)
    
    # Ensure period after year
    text = re.sub(r'(\(\d{4}(?:/\d{4})?\))\s*([A-Z])', r'\1. \2', text)
    
    # Fix double periods
    text = re.sub(r'\.\.$', '.', text)
    
    # Mark journal names for italicization using <<ITALIC_START>> and <<ITALIC_END>> markers
    # 
    # PATTERN 1: "Journal of X Y" or "International/African/etc Journal of X Y" (explicit journal names)
    # Matches hyphenated words like "Work-Integrated"
    text = re.sub(
        r'(\b(?:[A-Z][a-z]+\s+)?(?:International\s+)?(?:Multilingual\s+)?Journal\s+of\s+[A-Z][a-z]+(?:-[A-Z]?[a-z]+)?(?:\s+(?:and\s+)?[A-Z][a-zA-Z]+(?:-[A-Z]?[a-z]+)?)*)',
        r'<<ITALIC_START>>\1<<ITALIC_END>>',
        text
    )
    
    # PATTERN 2: Detect journal/publication name before volume/issue pattern
    # Matches: "Journal Name, Vol(Issue)" or "Journal Name, Vol"
    # This catches journals that don't have "Journal of" in their name
    # e.g., "Educational Research Review, 12(1)" or "Nature, 123"
    if '<<ITALIC_START>>' not in text:
        # Look for: ". Title Words, digits" pattern (journal name before volume)
        # Include hyphenated words
        text = re.sub(
            r'(\.\s+)([A-Z][a-z]+(?:-[A-Z]?[a-z]+)?(?:\s+(?:and\s+)?[A-Z]?[a-z]+(?:-[A-Z]?[a-z]+)?)*(?:\s+[A-Z][a-z]+(?:-[A-Z]?[a-z]+)?)*),\s*(\d+(?:\(\d+\))?)',
            r'\1<<ITALIC_START>>\2<<ITALIC_END>>, \3',
            text
        )
    
    # PATTERN 3: Books - title after year, before publisher location (heuristic)
    # Looking for title patterns: "(2020). Title of the book. City:"
    if '<<ITALIC_START>>' not in text:
        text = re.sub(
            r'(\(\d{4}(?:/\d{4})?\)\.\s+)([A-Z][^.]+?)(\.\s+[A-Z][a-z]+(?:,\s+[A-Z]{2})?:)',
            r'\1<<ITALIC_START>>\2<<ITALIC_END>>\3',
            text
        )
    
    return text

if __name__ == '__main__':
    refs = [
        'Bennett, D. (2021). The Future of Internships: Adapting to a New Normal. Journal of Career Development, 48(3), 234-245.',
        'Davis, K. (2020). Virtual Internships: Opportunities and Challenges. International Journal of Work-Integrated Learning, 21(2), 123-135.',
        'Gault, J. L., & Duey, M. (2010). Effects of Business Internships on Job Marketability. Journal of Education and Training, 52(1), 76-88.',
        'Lukman, Y. (2021). The University Internship Program and Its Effects. International Journal of Academe and Industry Research, 2(3), 86-101.',
        'Peter, G. (2011). The Impact of a Work Placement or Internship on Student Performance. International Journal of Management Education, 9(2), 32-40.',
        'Smith, J. (2020). A Study of Something Interesting. Educational Research Review, 12(1), 89-105.',
        'Ndamase, M. (2021). The Impact of Internship Programs. African Journal of Education, 19(2), 234-256.',
    ]
    
    print("Testing reference formatting...\n")
    
    for ref in refs:
        result = _format_single_apa_reference(ref)
        if '<<ITALIC_START>>' in result:
            match = re.search(r'<<ITALIC_START>>(.+?)<<ITALIC_END>>', result)
            print(f"OK - Italicized: '{match.group(1)}'")
        else:
            print(f"FAILED: {ref[:70]}...")
    
    print("\n--- Full formatted output ---\n")
    for ref in refs:
        result = _format_single_apa_reference(ref)
        print(result)
        print()
