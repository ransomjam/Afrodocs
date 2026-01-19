#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'pattern-formatter/backend')

import os
os.environ['FLASK_ENV'] = 'test'

from pattern_formatter_backend import DocumentProcessor

# Test with a very simple case first
content = "- Item 1\n- Item 2\n- Item 3"

processor = DocumentProcessor()
result = processor.process_text(content)
sections, _ = result

if isinstance(sections, dict) and 'analyzed' in sections:
    analyzed = sections['analyzed']
    print("Analyzed lines:")
    for line in analyzed:
        print(f"  Type: {line.get('type')}, Content: {line.get('content', '')[:50]}")
