#!/usr/bin/env python3
"""Test auto-increment numbering and bolding fixes"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import PatternFormatter

# Test case: numbered list with repeated numbers (should auto-increment)
test_content = """
1. Implications for Students:
Students face various challenges including academic pressure, social integration, and career planning.

1. Financial Considerations:
Managing university finances is crucial for student success.

1. Mental Health Support:
Universities must provide adequate mental health resources.

2. Recommendations:
The following recommendations are proposed.

2. Policy Changes:
New policies should be implemented.
"""

# Initialize formatter
formatter = PatternFormatter()

# Analyze and structure the content
structured_content = formatter.analyze_content(test_content)

print("=" * 60)
print("STRUCTURED CONTENT:")
print("=" * 60)
for section in structured_content:
    print(f"\nType: {section.get('type')}")
    print(f"Content: {section.get('content', section.get('items', ''))[:100]}")

# Generate document
formatter.clear_document()
formatter.add_structured_content(structured_content)

# Save
output_path = r'c:\Users\user\Desktop\PATTERN\test_numbering_output.docx'
formatter.save_document(output_path)
print(f"\n✅ Generated: {output_path}")
