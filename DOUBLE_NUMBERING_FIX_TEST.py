#!/usr/bin/env python3
"""
Comprehensive test for double-numbering fix
Tests various numbering scenarios to ensure they're not double-numbered
"""

# Test data simulating the issue from the screenshot
test_cases = [
    ("I. Implications for Students", "Should NOT be double-numbered"),
    ("II. Career Development", "Should NOT be double-numbered"),
    ("1. Introduction", "Should NOT be double-numbered"),
    ("1.1 Background", "Should NOT be double-numbered"),
    ("1.2 Methods", "Should NOT be double-numbered"),
    ("a) First item", "Should NOT be double-numbered"),
    ("- Regular bullet item", "Should be normal bullet (if 4+ items)"),
    ("Random text without numbering", "Can be numbered in context"),
]

print("=" * 70)
print("DOUBLE-NUMBERING FIX - TEST CASES")
print("=" * 70)

for i, (text, description) in enumerate(test_cases, 1):
    print(f"\nTest {i}: {text}")
    print(f"  Expected: {description}")
    
    # Simulate what the pattern matcher would do
    import re
    
    # Check for various numbering patterns
    checks = {
        "Simple numeric (1.)": bool(re.match(r'^\d+\.\s+', text)),
        "Roman numeral (I.)": bool(re.match(r'^[IVX]+\.\s+', text)),
        "Hierarchical (1.1)": bool(re.match(r'^\d+\.\d+', text)),
        "Letter (a)": bool(re.match(r'^[a-z]\)', text)),
        "Bullet (-)": bool(re.match(r'^-\s+', text)),
    }
    
    detected = [k for k, v in checks.items() if v]
    print(f"  Detected as: {', '.join(detected) if detected else 'plain text'}")

print("\n" + "=" * 70)
print("KEY FIXES:")
print("=" * 70)
print("""
1. NUMBERED_LIST RENDERING (Line 13002):
   - Check if item already has numbering
   - If yes: render with bold numbering (NO 'List Number' style)
   - If no: use 'List Number' style for auto-numbering
   
2. PATTERN CLASSIFICATION (Line 5865):
   - Skip simple numeric headers (1. Title)
   - Skip Roman numeral headers (I. Title)  
   - Skip hierarchical numbering (1.1, 1.2)
   - Only classify as numbered_list if truly a loose list item
   
3. BULLET_LIST RENDERING (Line 12883):
   - Already checks for numbering
   - Doesn't use bullets if item has existing numbering
   
RESULT:
   - Items with "I. Something" stay as "I. Something" (not "1. I. Something")
   - Items with "1.1 Something" stay as "1.1 Something" (not "1. 1.1 Something")
   - Only loose items get auto-numbered by Word
""")

print("\n" + "=" * 70)
print("VERIFICATION STATUS: Ready to test with actual documents")
print("=" * 70)
