#!/usr/bin/env python3
"""
Test script to verify formatting options are properly handled
"""
import requests
import json

# Test configuration
API_BASE = 'http://localhost:5000'
TEST_FILE = 'test_document.txt'

# Create a simple test document
test_content = """
Introduction

This is a test document for formatting options.

Main Section

This section contains some body text to test various formatting options
including font size, line spacing, and margins.

Subsection 1

Some more content here.

Subsection 2

Additional test content.

Conclusion

End of document.
"""

# Write test file
with open(TEST_FILE, 'w') as f:
    f.write(test_content)

print("Testing document formatting options...")
print("-" * 50)

# Test 1: With TOC and custom formatting
print("\nTest 1: Document with TOC, 14pt font, 2.0 line spacing, 3.0cm margins")
with open(TEST_FILE, 'rb') as f:
    files = {'file': f}
    data = {
        'include_toc': 'true',
        'font_size': '14',
        'line_spacing': '2.0',
        'margin_cm': '3.0'
    }
    response = requests.post(f'{API_BASE}/upload', files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Success! Job ID: {result.get('job_id')}")
        print(f"  Stats: {result.get('stats')}")
    else:
        print(f"✗ Failed with status {response.status_code}")
        print(f"  Response: {response.text}")

# Test 2: Without TOC, normal formatting
print("\nTest 2: Document without TOC, 12pt font, 1.5 line spacing, 2.5cm margins")
with open(TEST_FILE, 'rb') as f:
    files = {'file': f}
    data = {
        'include_toc': 'false',
        'font_size': '12',
        'line_spacing': '1.5',
        'margin_cm': '2.5'
    }
    response = requests.post(f'{API_BASE}/upload', files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Success! Job ID: {result.get('job_id')}")
        print(f"  Stats: {result.get('stats')}")
    else:
        print(f"✗ Failed with status {response.status_code}")
        print(f"  Response: {response.text}")

# Test 3: Small font, tight spacing, narrow margins
print("\nTest 3: Document with 10pt font, 1.0 line spacing, 0.5cm margins")
with open(TEST_FILE, 'rb') as f:
    files = {'file': f}
    data = {
        'include_toc': 'false',
        'font_size': '10',
        'line_spacing': '1.0',
        'margin_cm': '0.5'
    }
    response = requests.post(f'{API_BASE}/upload', files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ Success! Job ID: {result.get('job_id')}")
        print(f"  Stats: {result.get('stats')}")
    else:
        print(f"✗ Failed with status {response.status_code}")
        print(f"  Response: {response.text}")

print("\n" + "-" * 50)
print("Testing complete!")
