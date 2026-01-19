#!/usr/bin/env python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

# Set up logging to see error
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    from pattern_formatter_backend import DocumentProcessor
    from docx import Document
    
    processor = DocumentProcessor()
    
    print("Processing Sample with Certification.docx...")
    result = processor.process_docx('Samples/Sample with Certification.docx')
    print("Success!")
    
except NameError as e:
    print(f"NameError: {e}")
    import traceback
    traceback.print_exc()
    
    # Print current locals to see what's available
    print("\n\nLocal scope:")
    for k, v in locals().items():
        if not k.startswith('__'):
            print(f"  {k}: {type(v)}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
