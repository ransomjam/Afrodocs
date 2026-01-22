"""Debug script to check hierarchy preservation"""
from pattern_formatter_backend import DocumentProcessor
import logging
import re
import sys

logging.basicConfig(level=logging.WARNING)
sys.stdout.reconfigure(encoding='utf-8')

processor = DocumentProcessor()
result = processor.process_docx(r'C:\Users\user\Desktop\Afrodocs_dev\Afrodocs\Samples\sample_project_to_test.docx')

print('=== PROCESSED HEADINGS WITH HIERARCHIES ===')
pattern = re.compile(r'^(\d+(?:\.\d+)+)')

for line in result['lines']:
    if line.get('type') == 'heading':
        text = line.get('text', '')
        match = pattern.match(text)
        if match:
            depth = len(match.group(1).split('.'))
            print(f'[{depth} levels] {text[:80]}')

print('\n=== DEEP HIERARCHIES (3+ levels) ===')
for line in result['lines']:
    if line.get('type') == 'heading':
        text = line.get('text', '')
        match = pattern.match(text)
        if match:
            depth = len(match.group(1).split('.'))
            if depth >= 3:
                print(f'[{depth} levels] {text[:80]}')
