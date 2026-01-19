#!/usr/bin/env python3
"""
Extract and test formatter on actual sample documents - STANDALONE
"""

from docx import Document
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
                continue
        
        return text


def extract_chapter_one(doc_path):
    """Extract chapter one from document"""
    doc = Document(doc_path)
    text_parts = []
    
    in_chapter_one = False
    for para in doc.paragraphs:
        text = para.text.strip()
        
        # Detect chapter one start
        if 'chapter 1' in text.lower() or 'chapter one' in text.lower():
            in_chapter_one = True
        
        # Detect next chapter (stop collecting)
        if in_chapter_one and ('chapter 2' in text.lower() or 'chapter two' in text.lower()):
            break
        
        if in_chapter_one and text:
            text_parts.append(text)
    
    return '\n'.join(text_parts)


# Test on both sample documents
print("="*70)
print("TESTING FORMATTER ON ACTUAL SAMPLE DOCUMENTS")
print("="*70)

formatter = TextFormatterWithRegex()

# Sample 1
print("\n[SAMPLE 1] numbering and bulleting sample 1.docx")
print("-" * 70)

doc1_path = r"c:\Users\user\Desktop\PATTERN\Samples\numbering and bulleting sample 1.docx"
try:
    chapter1_text = extract_chapter_one(doc1_path)
    
    print("\nCHAPTER 1 - BEFORE (first 800 chars):")
    print(chapter1_text[:800])
    
    formatted = formatter.format_text(chapter1_text)
    
    print("\n\nCHAPTER 1 - AFTER (first 800 chars):")
    print(formatted[:800])
    
    # Count changes
    before_bolds = chapter1_text.count('**')
    after_bolds = formatted.count('**')
    
    print(f"\n\nBold markers: {before_bolds} -> {after_bolds} (added {after_bolds - before_bolds})")
    
    # Show differences
    print("\nDifferences detected:")
    before_lines = chapter1_text.split('\n')
    after_lines = formatted.split('\n')
    
    changes = 0
    for i, (before, after) in enumerate(zip(before_lines, after_lines), 1):
        if before != after and before.strip():
            print(f"\n  Line {i}:")
            print(f"    Before: {before[:100]}")
            print(f"    After:  {after[:100]}")
            changes += 1
            if changes >= 15:
                break
    
    if changes == 0:
        print("  NO CHANGES DETECTED - Formatter not matching content")
        print("\n  Sample lines that should match:")
        for line in before_lines[:20]:
            if line.strip():
                print(f"    '{line}'")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

print("\n\n" + "="*70)
