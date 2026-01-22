#!/usr/bin/env python3
"""Test the complete flow - paste text through API and generate Word document"""

import requests
import json
import sys
import os
from io import BytesIO

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

# Sample networking notes (shortened version for faster testing)
test_text = """## Networking Notes

### 1) What networking is

Networking is the practice of connecting computers, phones, servers, and devices so they can share data and resources (files, printers, internet access, applications).

## 6) Protocols and ports (quick reference)

| Protocol | Purpose                 | Transport | Common Port(s) |
| -------- | ----------------------- | --------: | -------------: |
| HTTP     | Web browsing            |       TCP |             80 |
| HTTPS    | Secure web              |       TCP |            443 |
| DNS      | Name resolution         |   UDP/TCP |             53 |
| DHCP     | Automatic IP assignment |       UDP |          67/68 |

## 14) Quick comparison tables

### 14.1 Switch vs Router

| Device       | Main Job                  | Works Mostly At |
| ------------ | ------------------------- | --------------- |
| Switch       | Connects devices in a LAN | Layer 2         |
| Router       | Connects networks         | Layer 3         |

### 14.2 TCP vs UDP

| Feature     | TCP                                 | UDP                              |
| ----------- | ----------------------------------- | -------------------------------- |
| Reliability | High (acknowledgements, retransmit) | Lower (no retransmit by default) |
| Speed       | Slower than UDP (overhead)          | Faster                           |
"""

def test_paste_and_format():
    """Test pasting text and formatting it"""
    print("=" * 60)
    print("Testing Paste and Format Flow")
    print("=" * 60)
    
    # Since this is plain text, we need to send it as a file or form data
    # Create a temporary text file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(test_text)
        temp_file = f.name
    
    try:
        # Upload via API (with mock auth - we'll use the test endpoint)
        files = {
            'file': open(temp_file, 'rb')
        }
        data = {
            'include_toc': 'false',
            'font_size': '12',
            'line_spacing': '1.5',
            'margin_cm': '2.5'
        }
        
        # For testing without auth, we'll test locally instead
        print("\nTesting through DocumentProcessor directly...")
        from pattern_formatter_backend import DocumentProcessor, FormatPolicy
        
        with open(temp_file, 'r') as f:
            text = f.read()
        
        policy = FormatPolicy()
        processor = DocumentProcessor(policy=policy)
        
        result = processor.process_text(text)
        if isinstance(result, tuple):
            structured_result = result[0]
        else:
            structured_result = result
        
        # Count tables in output
        table_count = 0
        for section in structured_result.get('structured', []):
            for item in section.get('content', []):
                if item.get('type') == 'table':
                    table_count += 1
                    print(f"\nFound table: {len(item.get('content', []))} rows")
        
        print(f"\nTotal tables in output: {table_count}")
        print(f"Expected: 3 tables")
        
        if table_count >= 3:
            # Now test Word generation
            print("\nGenerating Word document...")
            from pattern_formatter_backend import WordGenerator
            
            output_path = os.path.join(tempfile.gettempdir(), 'test_networking_notes.docx')
            generator = WordGenerator(policy=policy)
            generator.generate(
                structured_result.get('structured', []),
                output_path,
                images=[],
                font_size=12,
                line_spacing=1.5,
                margins={'left': 2.5, 'top': 2.5, 'bottom': 2.5, 'right': 2.5}
            )
            
            if os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                print(f"✓ Document generated: {output_path}")
                print(f"  File size: {file_size} bytes")
                return True
            else:
                print("✗ Failed to generate document")
                return False
        else:
            print("\n✗ Not all tables were detected")
            return False
            
    finally:
        os.unlink(temp_file)

if __name__ == '__main__':
    success = test_paste_and_format()
    sys.exit(0 if success else 1)
