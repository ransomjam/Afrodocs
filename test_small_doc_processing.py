#!/usr/bin/env python3
"""
Test script to identify page break issues in small documents
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import DocumentProcessor, PatternEngine
from docx import Document

def test_small_document_processing():
    """Test processing a small document to identify page break issues"""
    
    # Read the test content
    test_file = r"c:\Users\user\Desktop\PATTERN\test_small_document.txt"
    
    if not os.path.exists(test_file):
        print(f"Test file not found: {test_file}")
        return
    
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Testing small document processing...")
    print("=" * 50)
    print(f"Content length: {len(content)} characters")
    print(f"Word count: {len(content.split())} words")
    print("=" * 50)
    
    try:
        # Initialize the processor
        processor = DocumentProcessor()
        
        # Check if it's detected as a short document
        pattern_engine = PatternEngine()
        is_short, reason = pattern_engine.is_short_document(content)
        print(f"Is short document: {is_short}")
        print(f"Reason: {reason}")
        print("=" * 50)
        
        # Process the content
        lines = content.split('\n')
        print(f"Processing {len(lines)} lines...")
        
        # Create a new document
        doc = Document()
        
        # Process each line to see where page breaks might be added
        for i, line in enumerate(lines):
            line_type = processor._classify_line(line)
            print(f"Line {i+1:2d}: {line_type:15s} | {line[:60]}")
            
            # Check if this line would trigger a page break
            if hasattr(processor, '_should_add_page_break'):
                should_break = processor._should_add_page_break(line, line_type, is_short)
                if should_break:
                    print(f"         *** PAGE BREAK WOULD BE ADDED HERE ***")
        
        print("=" * 50)
        print("Test completed successfully!")
        
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_small_document_processing()