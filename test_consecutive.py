#!/usr/bin/env python3
"""Simple test to verify consecutive page breaks are fixed"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from docx import Document
from docx.oxml.ns import qn
from pattern_formatter_backend import DocumentProcessor, WordGenerator, FormatPolicy

test_text = '''
CHAPTER ONE
INTRODUCTION
Introduction content here.

CHAPTER TWO  
LITERATURE REVIEW
Literature review content.

CHAPTER THREE
METHODOLOGY
Methodology content.
'''

policy = FormatPolicy()
processor = DocumentProcessor(policy=policy)
result, images, shapes = processor.process_text(test_text)

output_path = 'pattern-formatter/backend/outputs/test_consecutive.docx'
generator = WordGenerator(policy=policy)
generator.generate(result['structured'], output_path, images=images, shapes=shapes, include_toc=True)

doc = Document(output_path)
page_breaks = []
for i, para in enumerate(doc.paragraphs):
    for run in para.runs:
        for elem in run._r.iter():
            if elem.tag == qn('w:br'):
                br_type = elem.get(qn('w:type'))
                if br_type == 'page':
                    page_breaks.append(i)

print('Page breaks at paragraphs:', page_breaks)

# Check for consecutive breaks
consecutive = 0
for i in range(len(page_breaks)-1):
    if page_breaks[i+1] == page_breaks[i] + 1:
        consecutive += 1

if consecutive == 0:
    print('SUCCESS: No consecutive page breaks')
else:
    print(f'WARNING: {consecutive} consecutive page break(s) found')
