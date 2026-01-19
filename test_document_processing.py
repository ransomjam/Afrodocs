#!/usr/bin/env python3
"""
Quick test script to process a sample document and identify the error
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import format_document

def test_document_processing():
    """Test processing a sample document"""
    
    # Use one of the sample documents
    sample_file = r"c:\Users\user\Desktop\PATTERN\samples\sample_dissertation.docx"
    
    if not os.path.exists(sample_file):
        print(f"Sample file not found: {sample_file}")
        return
    
    print(f"Testing document processing with: {sample_file}")
    print("=" * 50)
    
    try:
        # Test the format_document function directly
        result = format_document(sample_file)
        print("SUCCESS: Document processed successfully!")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_document_processing()