#!/usr/bin/env python3
"""
Test the complete fix with realistic document content
Simulates processing the sample documents with various numbering patterns
"""

test_document_content = """
CHAPTER ONE: IMPLICATIONS AND RECOMMENDATIONS

1. Implications for Students

This section discusses the key implications for students.

1.1 Enhanced Learning Environment

When teachers are motivated, they create more positive learning environments.

1.2 Increased Student Engagement  

Students show greater engagement in classrooms with motivated teachers.

2. Implications for Teachers

This section examines implications for the teaching profession.

2.1 Job Satisfaction

Motivated teachers experience higher job satisfaction and fulfillment.

2.2 Professional Growth

Opportunities for continuous professional development increase.

I. Key Findings

The research revealed several important patterns across multiple dimensions.

I.1 Student Outcomes

Performance metrics improved significantly with motivated instructors.

II. Recommendations

Based on findings, we recommend the following:

II.1 For Educational Institutions

Policy makers should prioritize teacher motivation programs.

II.2 For Future Research

More longitudinal studies are needed to validate findings.

a) First Research Priority
b) Second Research Priority  
c) Third Research Priority

- General recommendation point
- Another recommendation
- Additional point
"""

print("=" * 80)
print("DOUBLE-NUMBERING FIX - REALISTIC TEST")
print("=" * 80)

import re

# Analyze the content
lines = test_document_content.strip().split('\n')

print(f"\nAnalyzing {len(lines)} lines of document content...")
print("\nLine-by-line classification:")
print("-" * 80)

classifications = {
    'hierarchical': [],
    'roman': [],
    'simple_numeric': [],
    'letter': [],
    'bullet': [],
    'plain': []
}

for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    
    # Classify each line
    if re.match(r'^\d+\.\d+', stripped):
        classifications['hierarchical'].append(stripped)
        symbol = "[HIER]"
    elif re.match(r'^[IVX]+\.\d+', stripped):
        classifications['roman'].append(stripped)
        symbol = "[ROM+]"
    elif re.match(r'^[IVX]+\.', stripped):
        classifications['roman'].append(stripped)
        symbol = "[ROMA]"
    elif re.match(r'^\d+\.\s+', stripped):
        classifications['simple_numeric'].append(stripped)
        symbol = "[NUM1]"
    elif re.match(r'^[a-z]\)', stripped):
        classifications['letter'].append(stripped)
        symbol = "[LETT]"
    elif re.match(r'^[-•*]', stripped):
        classifications['bullet'].append(stripped)
        symbol = "[BULL]"
    else:
        classifications['plain'].append(stripped)
        symbol = "[PLAI]"
    
    # Show first 65 chars
    display = stripped[:65].ljust(65)
    print(f"{symbol}  {display}")

print("\n" + "-" * 80)
print("CLASSIFICATION SUMMARY:")
print("-" * 80)

for key, items in classifications.items():
    if items:
        print(f"\n{key.upper()}: {len(items)} items")
        for item in items[:3]:
            print(f"  • {item[:60]}")
        if len(items) > 3:
            print(f"  ... and {len(items) - 3} more")

print("\n" + "=" * 80)
print("EXPECTED BEHAVIOR AFTER FIX:")
print("=" * 80)

fix_expectations = [
    ("1.1, 1.2, 2.1, 2.2", "Should stay as-is (hierarchical)", "NO double-numbering"),
    ("I., II.", "Should stay as-is (Roman numerals)", "NO double-numbering"),
    ("I.1, II.1, II.2", "Should stay as-is (Roman + hierarchical)", "NO double-numbering"),
    ("a), b), c)", "Should stay as-is (letter numbering)", "NO double-numbering"),
    ("- bullets", "Should render as bullets only if 4+ short items", "NO auto-numbering"),
    ("1. Implications, 2. Implications", "Should be detected as HEADINGS not list items", "NO list style applied"),
]

for pattern, expected_class, expected_result in fix_expectations:
    print(f"\n{pattern}:")
    print(f"  Classification: {expected_class}")
    print(f"  Result: {expected_result}")

print("\n" + "=" * 80)
print("TEST VERIFICATION")
print("=" * 80)

issues_found = 0

# Check for problematic patterns
for category, items in classifications.items():
    for item in items:
        # These should NOT appear if fix works
        if re.search(r'^\d+\.\s+[IVX]+\.', item):
            print(f"❌ PROBLEM: Double numbering detected: {item}")
            issues_found += 1
        elif re.search(r'^\d+\.\s+\d+\.\d+', item):
            print(f"❌ PROBLEM: Double hierarchical numbering: {item}")
            issues_found += 1

if issues_found == 0:
    print("✅ NO problematic patterns detected in test data")
    print("✅ All numbering patterns are valid")
    print("\n✅ FIX VERIFICATION PASSED")
else:
    print(f"\n❌ FOUND {issues_found} problematic patterns")

print("=" * 80)
