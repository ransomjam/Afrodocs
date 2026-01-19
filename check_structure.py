#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

content = """# Section A

- Item 1
- Item 2  
- Item 3
"""

processor = DocumentProcessor()
result = processor.process_text(content)

print(f"Result type: {type(result)}")
print(f"Result length: {len(result) if isinstance(result, tuple) else 'N/A'}")

if isinstance(result, tuple):
    sections, metadata = result
    print(f"Sections type: {type(sections)}")
    print(f"Sections: {sections}")
