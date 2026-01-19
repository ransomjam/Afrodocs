#!/usr/bin/env python3
"""
Simple test script to test document processing via the API endpoint
"""

import requests
import os

def test_document_upload():
    """Test uploading and processing a sample document via API"""
    
    # Use one of the sample documents
    sample_file = r"c:\Users\user\Desktop\PATTERN\samples\sample_dissertation.docx"
    
    if not os.path.exists(sample_file):
        print(f"Sample file not found: {sample_file}")
        return
    
    print(f"Testing document upload with: {sample_file}")
    print("=" * 50)
    
    try:
        # Start the server first (this will fail if server isn't running)
        url = "http://localhost:5000/upload"
        
        # Prepare the file for upload
        with open(sample_file, 'rb') as f:
            files = {'file': f}
            
            print("Uploading document...")
            response = requests.post(url, files=files, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                print("SUCCESS: Document processed successfully!")
                print(f"Result: {result}")
            else:
                print(f"ERROR: HTTP {response.status_code}")
                print(f"Response: {response.text}")
                
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to server. Is the server running on localhost:5000?")
        print("Try running: py pattern-formatter/backend/pattern_formatter_backend.py")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_document_upload()