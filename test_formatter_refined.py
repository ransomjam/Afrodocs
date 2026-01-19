#!/usr/bin/env python3
"""Direct test of TextFormatterWithRegex patterns - REFINED"""

import re

class TextFormatterWithRegex:
    """Applies 6 powerful regex patterns to auto-bold numbered/bulleted topics"""
    
    def __init__(self):
        self.patterns = [
            {
                'regex': r'^(#{1,3}\s+)(\d+\.\s+)(\d+\.\s+)([A-Z][A-Za-z\s\-]+:)',
                'replacement': r'\1**\3\4**',
                'name': 'Double-numbered items',
                'flags': re.MULTILINE
            },
            {
                'regex': r'^(#{1,3}\s+)(\d+\.\s+)([A-Z][A-Za-z\s\-]+:)$',
                'replacement': r'\1**\2\3**',
                'name': 'Heading items with numbers',
                'flags': re.MULTILINE
            },
            {
                'regex': r'^(\d+\.\s+[A-Z][A-Za-z\s\-]+:)\s*$',
                'replacement': r'**\1**',
                'name': 'Standalone numbered topics',
                'flags': re.MULTILINE
            },
            {
                'regex': r'^(#{1,3}\s+)([IVX]+\.\s+)([A-Z][A-Za-z\s\-]+:)$',
                'replacement': r'\1**\2\3**',
                'name': 'Roman numeral headings',
                'flags': re.MULTILINE
            },
            {
                'regex': r'^(-\s+)([A-Z][A-Za-z\s\-]+)$',
                'replacement': r'\1**\2**',
                'name': 'Bulleted terms',
                'flags': re.MULTILINE
            },
            {
                'regex': r'^(\d+\.\s+[A-Z][A-Za-z\s\-]+)$',
                'replacement': r'**\1**',
                'name': 'Numbered lists without colons',
                'flags': re.MULTILINE
            },
        ]
    
    def format_text(self, text):
        if not text:
            return text
        
        for pattern_config in self.patterns:
            try:
                regex = pattern_config['regex']
                replacement = pattern_config['replacement']
                flags = pattern_config['flags']
                text = re.sub(regex, replacement, text, flags=flags)
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        return text


# Run tests
formatter = TextFormatterWithRegex()

print("="*60)
print("REGEX TEXT FORMATTER TEST SUITE - REFINED")
print("="*60)

# Test 1: Double numbering fix
print("\n[TEST 1] Double-Numbering Fix (Pattern 3)")
text = "# 1. 2. Introduction:"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '**2. Introduction:**' in result else '[FAIL]'}")

# Test 2: Heading numbered items
print("\n[TEST 2] Heading Numbered Items (Pattern 1)")
text = "# 1. Research Methods:"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '**1. Research Methods:**' in result else '[FAIL]'}")

# Test 3: Standalone numbered
print("\n[TEST 3] Standalone Numbered Topics (Pattern 2)")
text = "1. Introduction:"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '**1. Introduction:**' in result else '[FAIL]'}")

# Test 4: Roman numerals
print("\n[TEST 4] Roman Numerals (Pattern 6)")
text = "# I. Introduction:"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '**I. Introduction:**' in result else '[FAIL]'}")

# Test 5: Bulleted terms
print("\n[TEST 5] Bulleted Terms (Pattern 4)")
text = "- Research Method"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '- **Research Method**' in result else '[FAIL]'}")

# Test 6: Numbered lists no colons
print("\n[TEST 6] Numbered Lists Without Colons (Pattern 5)")
text = "1. Introduction Method"
result = formatter.format_text(text)
print(f"Input:  {text}")
print(f"Output: {result}")
print(f"Status: {'[PASS]' if '**1. Introduction Method**' in result else '[FAIL]'}")

# Test 7: Complex document
print("\n[TEST 7] Complex Document (All Patterns)")
text = """## 2. Key Objectives

1. Establish Research Framework
2. Gather Data

- Literature Review
- Primary Research

# I. Findings"""

result = formatter.format_text(text)
print(f"Input has {len(text)} chars, output has {len(result)} chars")

# Count bolded items
bold_count = result.count('**')
print(f"Bolded items: {bold_count // 2}")
print(f"Status: {'[PASS]' if bold_count >= 4 else '[FAIL]'}")

print("\n" + "="*60)
print("TEST COMPLETE")
print("="*60)
