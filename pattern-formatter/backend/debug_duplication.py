"""Debug duplication issue in Chapter 1"""
from pattern_formatter_backend import DocumentProcessor
import logging
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
logging.disable(logging.CRITICAL)

processor = DocumentProcessor()
result, _, _ = processor.process_docx(r'C:\Users\user\Desktop\Afrodocs_dev\Afrodocs\Samples\sample_project_to_test.docx')

# Check structured output  
structured = result.get('structured', [])
print(f'=== STRUCTURED OUTPUT: Detailed Chapter 1 Sections ===')

for i, section in enumerate(structured):
    if isinstance(section, dict):
        heading = section.get('heading', '')
        content = section.get('content', [])
        # Print detailed info for sections 1.4.2, 1.5, 1.6
        if heading.startswith('1.4.2') or heading.startswith('1.5') or heading.startswith('1.6'):
            print(f"\n=== [{i}] Section: {heading} ===")
            print(f"Content items: {len(content)}")
            for j, c in enumerate(content):
                if isinstance(c, dict):
                    c_type = c.get('type', '')
                    c_text = c.get('text', '') or c.get('content', '')
                    print(f"\n  [{j}] Type: {c_type}")
                    print(f"      Text: {c_text[:100] if c_text else '(empty)'}")
                    if c_type == 'numbered_list':
                        items = c.get('items', [])
                        print(f"      Items count: {len(items)}")
                        for k, item in enumerate(items):
                            if isinstance(item, dict):
                                print(f"        [{k}] {item.get('content', '')[:60]}")
                            else:
                                print(f"        [{k}] {str(item)[:60]}")
