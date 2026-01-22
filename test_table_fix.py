#!/usr/bin/env python3
"""Test script to verify markdown table handling in plain text paste"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import DocumentProcessor, FormatPolicy

# Sample networking notes with pipe-delimited tables
test_text = """## Networking Notes

### 1) What networking is

Networking is the practice of connecting computers, phones, servers, and devices so they can share data and resources (files, printers, internet access, applications). It involves hardware, software, rules (protocols), and processes that keep communication reliable and secure.

## 6) Protocols and ports (quick reference)

| Protocol | Purpose                 | Transport | Common Port(s) |
| -------- | ----------------------- | --------: | -------------: |
| HTTP     | Web browsing            |       TCP |             80 |
| HTTPS    | Secure web              |       TCP |            443 |
| DNS      | Name resolution         |   UDP/TCP |             53 |
| DHCP     | Automatic IP assignment |       UDP |          67/68 |
| SSH      | Secure remote login     |       TCP |             22 |
| FTP      | File transfer           |       TCP |             21 |

**Notes**

* TCP is connection-oriented (reliable, ordered delivery).
* UDP is connectionless (faster, less overhead, used for streaming/DNS).

---

## 14) Quick comparison tables

### 14.1 Switch vs Router vs Access Point

| Device       | Main Job                  | Works Mostly At | Typical Use                        |
| ------------ | ------------------------- | --------------- | ---------------------------------- |
| Switch       | Connects devices in a LAN | Layer 2         | Office/classroom wiring            |
| Router       | Connects networks         | Layer 3         | LAN to Internet, LAN to LAN        |
| Access Point | Provides Wi-Fi            | Layer 2         | Wireless access for phones/laptops |

### 14.2 TCP vs UDP

| Feature     | TCP                                 | UDP                              |
| ----------- | ----------------------------------- | -------------------------------- |
| Reliability | High (acknowledgements, retransmit) | Lower (no retransmit by default) |
| Speed       | Slower than UDP (overhead)          | Faster                           |
| Best for    | Web, email, file transfer           | Streaming, voice, DNS            |
"""

def test_markdown_tables():
    """Test that markdown tables are properly detected and structured"""
    print("=" * 60)
    print("Testing Markdown Table Detection")
    print("=" * 60)
    
    policy = FormatPolicy()
    processor = DocumentProcessor(policy=policy)
    
    # Process text
    result = processor.process_text(test_text)
    if isinstance(result, tuple):
        structured = result[0]['structured']
    else:
        structured = result['structured']
    
    # Count tables
    table_count = 0
    for section in structured:
        if not isinstance(section, dict):
            continue
        for item in section.get('content', []):
            if isinstance(item, dict) and item.get('type') == 'table':
                table_count += 1
                print(f"\nFound table with {len(item.get('content', []))} rows")
                # Print first few rows
                for row_idx, row in enumerate(item.get('content', [])[:3]):
                    if row.get('type') == 'row':
                        cells = row.get('cells', [])
                        print(f"  Row {row_idx}: {cells[:2]}...")  # Print first 2 cells
    
    print(f"\nTotal tables detected: {table_count}")
    print("Expected: 3 tables")
    
    if table_count >= 3:
        print("\n✓ SUCCESS: All tables detected and included!")
        return True
    else:
        print("\n✗ FAILED: Not all tables were detected.")
        return False

if __name__ == '__main__':
    success = test_markdown_tables()
    sys.exit(0 if success else 1)
