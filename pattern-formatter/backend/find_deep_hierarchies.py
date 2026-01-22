"""Find deep hierarchies in original document and compare to processed output"""
from docx import Document
from pattern_formatter_backend import DocumentProcessor
import logging
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
logging.disable(logging.CRITICAL)

doc = Document(r'C:\Users\user\Desktop\Afrodocs_dev\Afrodocs\Samples\sample_project_to_test.docx')
pattern = re.compile(r'^(\d+(?:\.\d+){2,})')  # 3+ levels

print("=== ORIGINAL DOCUMENT: DEEP HIERARCHIES (3+ levels) ===")
original_deep = []
for p in doc.paragraphs:
    text = p.text.strip()
    m = pattern.match(text)
    if m:
        num = m.group(1)
        depth = len(num.split('.'))
        original_deep.append((num, text[:70]))
        print(f'[{depth} levels] {text[:80]}')

print(f"\nTotal deep hierarchies in original: {len(original_deep)}")

# Now process and compare
print("\n=== PROCESSED OUTPUT: HEADINGS WITH DEEP HIERARCHIES ===")
processor = DocumentProcessor()
result, _, _ = processor.process_docx(r'C:\Users\user\Desktop\Afrodocs_dev\Afrodocs\Samples\sample_project_to_test.docx')

# Debug: Check what result actually is
print(f"Result type: {type(result)}")
if isinstance(result, dict):
    print(f"Result keys: {result.keys()}")
    lines = result.get('analyzed', [])  # Fixed: use 'analyzed' key
else:
    lines = result
print(f"Lines count: {len(lines)}")

processed_deep = []
for line in lines:
    if isinstance(line, dict) and line.get('type') in ['heading', 'heading_hierarchy', 'chapter_heading']:
        text = line.get('text', '')
        m = pattern.match(text)
        if m:
            num = m.group(1)
            depth = len(num.split('.'))
            processed_deep.append((num, text[:70]))
            print(f'[{depth} levels] {text[:80]}')

print(f"\nTotal deep hierarchies in processed: {len(processed_deep)}")
print(f"\nLOST: {len(original_deep) - len(processed_deep)} deep hierarchies")

# Debug: show all headings 
print("\n=== ALL PROCESSED HEADINGS (showing text and content) ===")
search_terms = ['Main Research', 'Digital Preservation', 'Digital Migration', 'Digital Replication', 'Scope of']
for line in lines:
    if isinstance(line, dict) and line.get('type') in ['heading', 'heading_hierarchy', 'chapter_heading']:
        text = line.get('text', '')
        content = line.get('content', '')
        original = line.get('original', '')
        # Check both text and content
        for term in search_terms:
            if term.lower() in text.lower() or term.lower() in content.lower() or term.lower() in original.lower():
                print(f"  text='{text[:60]}' | content='{content[:60]}' | original='{original[:60]}'")

