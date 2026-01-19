#!/usr/bin/env python
import sys
import os
import traceback

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

# Import and test
try:
    from pattern_formatter_backend import DocumentProcessor
    
    doc_processor = DocumentProcessor()
    result = doc_processor.process_document('Samples/Sample with Certification.docx')
    print("Success!")
    print(result)
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    print("\nFull Traceback:")
    traceback.print_exc()
