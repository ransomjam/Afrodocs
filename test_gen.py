#!/usr/bin/env python

import sys
sys.path.insert(0, 'pattern-formatter/backend')

from pattern_formatter_backend import DocumentProcessor, WordGenerator
import logging
import traceback

logging.basicConfig(level=logging.WARNING)

try:
    # Read the test file
    with open('test_formatting.txt', 'r') as f:
        content = f.read()

    print('✓ Read test file')

    # Process it
    processor = DocumentProcessor()
    analyzed = processor.process_text(content)

    print(f'✓ Processed document, analyzed lines: {len(analyzed)}')

    # Generate Word document
    generator = WordGenerator()
    output_path = 'test_formatting_output.docx'
    generator.generate(
        analyzed,
        output_path,
        font_size=12,
        line_spacing=1.5
    )
    
    print(f'✓ Generated: {output_path}')

except Exception as e:
    print(f'✗ Error: {e}')
    traceback.print_exc()
