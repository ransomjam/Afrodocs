#!/usr/bin/env python
"""Test structure preservation for intelligent paste box"""

import sys
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import DocumentProcessor

# Test case: Mixed structured content like what would be pasted
test_content = """Discussions of Findings

This section presents the key findings from our research methodology and analysis.

**Rewards**

Rewards represent one of the most critical components of our study. They serve as both incentive mechanisms and performance indicators.

1. Implications for Students:

a. Improved academic performance through better resource allocation
b. Enhanced engagement with course materials
c. Stronger connections with peer support networks
d. Better understanding of personal learning styles

---

2. Institutional Benefits:

a. More effective curriculum design based on empirical data
b. Better resource planning and budget allocation
c. Improved student retention rates
d. Enhanced reputation and accreditation standing

**Challenges and Limitations**

Our research identified several important challenges that warrant discussion.

- Time constraints limited the depth of analysis
- Resource limitations affected sample size
- Institutional policy changes mid-study required adaptation
- Technology infrastructure limitations

---

**Conclusions**

The structured approach demonstrated significant improvements across all measured dimensions.
"""

# Initialize processor
processor = DocumentProcessor()

# Test just the _preserve_markdown_structure method
print("=" * 80)
print("STEP 1: _preserve_markdown_structure()")
print("=" * 80)
preserved_step1 = processor._preserve_markdown_structure(test_content)

markers_step1 = {
    '[MARKDOWN_BOLD]': preserved_step1.count('[MARKDOWN_BOLD]'),
    '[NUMBERED_HEADER]': preserved_step1.count('[NUMBERED_HEADER]'),
    '[INDENT_ITEM]': preserved_step1.count('[INDENT_ITEM]'),
}

print("Markers detected after step 1:")
for marker, count in markers_step1.items():
    print(f"  {marker}: {count}")

# Test the _mark_section_breaks method on preserved text
print("\n" + "=" * 80)
print("STEP 2: _mark_section_breaks()")
print("=" * 80)
marked_step2 = processor._mark_section_breaks(preserved_step1)

markers_step2 = {
    '[MARKDOWN_BOLD]': marked_step2.count('[MARKDOWN_BOLD]'),
    '[NUMBERED_HEADER]': marked_step2.count('[NUMBERED_HEADER]'),
    '[INDENT_ITEM]': marked_step2.count('[INDENT_ITEM]'),
    '[SECTION_BREAK]': marked_step2.count('[SECTION_BREAK]'),
}

print("Markers detected after step 2:")
for marker, count in markers_step2.items():
    print(f"  {marker}: {count}")

# Show lines with section breaks
print("\nLines with [SECTION_BREAK]:")
for i, line in enumerate(marked_step2.split('\n')):
    if '[SECTION_BREAK]' in line:
        print(f"  Line {i+1}: {repr(line)}")

# Simulate the full process_text pipeline
print("\n" + "=" * 80)
print("FULL process_text() PIPELINE")
print("=" * 80)
try:
    result = processor.process_text(test_content)
    
    # Result is (dict_with_analyzed_key, images_list)
    result_dict = result[0] if isinstance(result, tuple) else result
    analyzed_lines = result_dict.get('analyzed', []) if isinstance(result_dict, dict) else result_dict
    
    print(f"SUCCESS: process_text() completed successfully")
    print(f"  Total lines analyzed: {len(analyzed_lines)}")
    
    # Count line types
    type_counts = {}
    for line_data in analyzed_lines:
        if isinstance(line_data, dict):
            line_type = line_data.get('type', 'unknown')
            type_counts[line_type] = type_counts.get(line_type, 0) + 1
    
    print(f"\nLine types detected:")
    for line_type, count in sorted(type_counts.items()):
        print(f"  {line_type}: {count}")
    
    # Show shortdoc_header lines
    print(f"\nLines classified as 'shortdoc_header':")
    header_lines = [l for l in analyzed_lines if isinstance(l, dict) and l.get('type') == 'shortdoc_header']
    for i, line in enumerate(header_lines[:10]):
        text = line.get('content', '')[:60]
        bold = line.get('should_be_bold', False)
        metadata = line.get('from_metadata', 'none')
        print(f"  {i+1}. {text}... (bold={bold}, metadata={metadata})")
        
except Exception as e:
    print(f"ERROR in process_text(): {e}")
    import traceback
    traceback.print_exc()
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)

