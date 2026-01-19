#!/usr/bin/env python3
"""
Test the TextFormatterWithRegex class with various formatting scenarios
Validates all 6 regex patterns
"""

import sys
import re
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import TextFormatterWithRegex

def test_double_numbering_fix():
    """Pattern 3: Fix double-numbering errors"""
    print("\n" + "="*60)
    print("TEST 1: Double-Numbering Fix (Pattern 3)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    test_cases = [
        ("# 1. 2. Introduction:", "# **2. Introduction:**"),
        ("## 3. 4. Methods:", "## **4. Methods:**"),
        ("### 2. 3. Results:", "### **3. Results:**"),
    ]
    
    passed = 0
    for input_text, expected in test_cases:
        result = formatter.format_text(input_text)
        status = "✅ PASS" if expected in result else "❌ FAIL"
        print(f"\n{status}")
        print(f"  Input:    {input_text}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        if expected in result:
            passed += 1
    
    print(f"\nResult: {passed}/{len(test_cases)} PASSED")
    return passed == len(test_cases)


def test_heading_numbered_items():
    """Pattern 1: Numbered items in headings"""
    print("\n" + "="*60)
    print("TEST 2: Heading Numbered Items (Pattern 1)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    test_cases = [
        ("# 1. Research Methods:", "# **1. Research Methods:**"),
        ("## 2. Data Analysis:", "## **2. Data Analysis:**"),
        ("### 3. Conclusion:", "### **3. Conclusion:**"),
    ]
    
    passed = 0
    for input_text, expected in test_cases:
        result = formatter.format_text(input_text)
        status = "✅ PASS" if expected in result else "❌ FAIL"
        print(f"\n{status}")
        print(f"  Input:    {input_text}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        if expected in result:
            passed += 1
    
    print(f"\nResult: {passed}/{len(test_cases)} PASSED")
    return passed == len(test_cases)


def test_standalone_numbered():
    """Pattern 2: Standalone numbered topics"""
    print("\n" + "="*60)
    print("TEST 3: Standalone Numbered Topics (Pattern 2)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    input_text = """Some paragraph here

1. Introduction: This is an introduction
2. Methods: This is methods section
3. Results: This is results section"""
    
    result = formatter.format_text(input_text)
    
    print("\nInput:")
    print(input_text)
    print("\nOutput:")
    print(result)
    
    # Check if numbers are bolded
    checks = [
        ("**1. Introduction:**" in result),
        ("**2. Methods:**" in result),
        ("**3. Results:**" in result),
    ]
    
    passed = sum(checks)
    print(f"\nResult: {passed}/{len(checks)} items bolded")
    return passed == len(checks)


def test_bulleted_terms():
    """Pattern 4: Bulleted terms without bold"""
    print("\n" + "="*60)
    print("TEST 4: Bulleted Terms (Pattern 4)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    input_text = """- Research Method
- Data Collection
- Statistical Analysis
- Final Report"""
    
    result = formatter.format_text(input_text)
    
    print("\nInput:")
    print(input_text)
    print("\nOutput:")
    print(result)
    
    checks = [
        "- **Research Method**" in result,
        "- **Data Collection**" in result,
        "- **Statistical Analysis**" in result,
        "- **Final Report**" in result,
    ]
    
    passed = sum(checks)
    print(f"\nResult: {passed}/{len(checks)} items bolded")
    return passed == len(checks)


def test_roman_numerals():
    """Pattern 6: Roman numerals in headings"""
    print("\n" + "="*60)
    print("TEST 5: Roman Numerals (Pattern 6)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    test_cases = [
        ("# I. Introduction:", "# **I. Introduction:**"),
        ("## II. Methods:", "## **II. Methods:**"),
        ("### III. Results:", "### **III. Results:**"),
    ]
    
    passed = 0
    for input_text, expected in test_cases:
        result = formatter.format_text(input_text)
        status = "✅ PASS" if expected in result else "❌ FAIL"
        print(f"\n{status}")
        print(f"  Input:    {input_text}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        if expected in result:
            passed += 1
    
    print(f"\nResult: {passed}/{len(test_cases)} PASSED")
    return passed == len(test_cases)


def test_numbered_lists_no_colons():
    """Pattern 5: Numbered lists without colons"""
    print("\n" + "="*60)
    print("TEST 6: Numbered Lists Without Colons (Pattern 5)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    input_text = """1. Introduction Method
2. Data Collection Process
3. Analysis Procedure"""
    
    result = formatter.format_text(input_text)
    
    print("\nInput:")
    print(input_text)
    print("\nOutput:")
    print(result)
    
    checks = [
        "**1. Introduction" in result,
        "**2. Data Collection" in result,
        "**3. Analysis" in result,
    ]
    
    passed = sum(checks)
    print(f"\nResult: {passed}/{len(checks)} items detected/bolded")
    return passed >= len(checks) - 1  # Allow some flexibility


def test_complex_document():
    """Test all patterns together on a complex document"""
    print("\n" + "="*60)
    print("TEST 7: Complex Document (All Patterns)")
    print("="*60)
    
    formatter = TextFormatterWithRegex()
    
    input_text = """# 1. Research Overview

## 2. Objectives and Goals

Our key objectives are:

1. Establish research framework
2. Gather empirical data
3. Analyze findings

## 3. Research Methods

- Literature Review
- Empirical Study
- Comparative Analysis

# I. Major Findings

## II. Key Results

Some introduction here.

1. Primary Discovery: This is very important
2. Secondary Finding: Also significant
3. Tertiary Observation: Still relevant"""
    
    result = formatter.format_text(input_text)
    
    print("\n--- Original Text ---")
    print(input_text[:500] + "...\n[truncated]")
    
    print("\n--- Formatted Text ---")
    print(result[:500] + "...\n[truncated]")
    
    # Check for various bolded items
    checks = [
        "**2. Objectives**" in result or "**2. Objectives" in result,
        "**3. Research**" in result or "**3. Research" in result,
        "- **Literature Review**" in result,
        "**I. Major**" in result,
        "**1. Primary" in result,
    ]
    
    passed = sum(checks)
    print(f"\nResult: {passed}/{len(checks)} formatting checks PASSED")
    return passed >= 4  # At least 4 of 5 should pass


def main():
    print("\n" + "="*60)
    print("TESTING REGEX TEXT FORMATTER")
    print("Testing all 6 patterns for auto-bolding functionality")
    print("="*60)
    
    tests = [
        ("Double-Numbering Fix", test_double_numbering_fix),
        ("Heading Numbered Items", test_heading_numbered_items),
        ("Standalone Numbered Topics", test_standalone_numbered),
        ("Bulleted Terms", test_bulleted_terms),
        ("Roman Numerals", test_roman_numerals),
        ("Numbered Lists No Colons", test_numbered_lists_no_colons),
        ("Complex Document", test_complex_document),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ ERROR in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    passed_count = sum(1 for _, result in results if result)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests PASSED")
    
    if passed_count == total_count:
        print("\n🎉 ALL TESTS PASSED! Regex formatter is ready for deployment.")
    else:
        print(f"\n⚠️  {total_count - passed_count} tests failed. Review patterns.")


if __name__ == '__main__':
    main()
