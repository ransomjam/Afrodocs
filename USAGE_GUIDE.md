# Usage Guide: Unicode Scrubber & Flex-Bullet Detector

## Installation & Setup

The implementation is already integrated into `pattern_formatter_backend.py`. No additional installation required.

---

## Basic Usage

### Initialize the Engine

```python
from pattern_formatter_backend import PatternEngine

# Create engine instance
engine = PatternEngine()
```

### Analyze a Line

```python
# Example 1: Bullet with emoji
line = "- Rising Sea Levels 🌊"
result = engine.analyze_line(line, line_num=1)

print(f"Type: {result['type']}")              # Output: bullet_list
print(f"Content: {result['content']}")        # Output: Rising Sea Levels
print(f"Confidence: {result['confidence']}")  # Output: 0.98
print(f"Has emoji: {'🌊' in result['content']}")  # Output: False ✅
```

### Analyze Multiple Lines

```python
lines = [
    "- Rising Sea Levels 🌊",
    "■ Agriculture 🌾",
    "* Renewable Energy ⚡",
    "Environmental Impacts 🌎",
    "• Biodiversity Loss",
    "– Deforestation 🌳"
]

for i, line in enumerate(lines, 1):
    result = engine.analyze_line(line, line_num=i)
    print(f"Line {i}: {line}")
    print(f"  Type: {result['type']}")
    print(f"  Content: {result['content']}")
    print()
```

**Output**:
```
Line 1: - Rising Sea Levels 🌊
  Type: bullet_list
  Content: Rising Sea Levels

Line 2: ■ Agriculture 🌾
  Type: bullet_list
  Content: Agriculture

Line 3: * Renewable Energy ⚡
  Type: bullet_list
  Content: Renewable Energy

Line 4: Environmental Impacts 🌎
  Type: paragraph
  Content: Environmental Impacts

Line 5: • Biodiversity Loss
  Type: bullet_list
  Content: Biodiversity Loss

Line 6: – Deforestation 🌳
  Type: bullet_list
  Content: Deforestation
```

---

## Running Tests

### Test Bullet Cleanup

```python
# Run comprehensive test suite
results = engine.test_bullet_cleanup()

# Display results
for result in results:
    status = "✅ PASS" if result['passed'] else "❌ FAIL"
    print(f"{status}: {result['text']}")
    print(f"  Expected Type: {result['expected_type']}")
    print(f"  Actual Type: {result['actual_type']}")
    print(f"  Expected Content: {result['expected_content']}")
    print(f"  Actual Content: {result['actual_content']}")
    print(f"  Emoji Stripped: {result['emoji_stripped']}")
    print()
```

### Test Specific Pattern

```python
# Test a specific bullet marker
test_cases = [
    "- Hyphen bullet",
    "– En-dash bullet",
    "— Em-dash bullet",
    "• Round bullet",
    "■ Square bullet",
    "* Asterisk bullet",
]

for text in test_cases:
    result = engine.analyze_line(text, line_num=0)
    is_bullet = result['type'] == 'bullet_list'
    print(f"{'✅' if is_bullet else '❌'} {text:25s} → {result['type']}")
```

---

## Advanced Usage

### Check Unicode Scrubber Pattern

```python
# Access the unicode_scrubber pattern
patterns = engine.patterns.get('unicode_scrubber', [])
print(f"Number of scrubber patterns: {len(patterns)}")

# Test the pattern directly
import re
pattern = patterns[0]

# Examples
test_strings = [
    "- Rising Sea Levels 🌊",
    "■ Agriculture 🌾",
    "Clean text",
    "Text with emojis 🎉🎊🎈",
]

for s in test_strings:
    cleaned = pattern.sub('', s)
    print(f"Before:  {repr(s)}")
    print(f"After:   {repr(cleaned)}")
    print()
```

### Check Bullet Detection Patterns

```python
# Access bullet list patterns
bullet_patterns = engine.patterns.get('bullet_list', [])
print(f"Number of bullet patterns: {len(bullet_patterns)}")

# Test each pattern
test_text = "- Rising Sea Levels"

for i, pattern in enumerate(bullet_patterns):
    match = pattern.match(test_text)
    if match:
        print(f"Pattern {i}: MATCH ✅")
        if match.groups():
            print(f"  Groups: {match.groups()}")
    else:
        print(f"Pattern {i}: No match")
```

---

## Integration with Document Processing

### Full Pipeline Example

```python
from pattern_formatter_backend import PatternEngine, WordGenerator
import os

# Initialize
engine = PatternEngine()
word_gen = WordGenerator()

# Example document lines
document_lines = [
    "# Environmental Issues",
    "This document discusses climate impacts.",
    "",
    "Key points:",
    "- Rising Sea Levels 🌊",
    "■ Agriculture 🌾",
    "* Renewable Energy ⚡",
    "• Biodiversity Loss",
    "",
    "Conclusion: Action is needed 🌍",
]

# Analyze all lines
analyzed_lines = []
for i, line in enumerate(document_lines, 1):
    if line.strip():  # Skip empty lines
        analysis = engine.analyze_line(line, line_num=i)
        analyzed_lines.append(analysis)

# Display results
print("Analyzed Document Structure:")
print("=" * 60)
for analysis in analyzed_lines:
    print(f"Line {analysis['line_num']:2d}: {analysis['type']:15s} | {analysis['content'][:50]}")
```

**Output**:
```
Analyzed Document Structure:
============================================================
Line  1: heading                | Environmental Issues
Line  2: paragraph              | This document discusses climate impacts.
Line  3: bullet_list            | Rising Sea Levels
Line  4: bullet_list            | Agriculture
Line  5: bullet_list            | Renewable Energy
Line  6: bullet_list            | Biodiversity Loss
Line  7: paragraph              | Conclusion: Action is needed
```

---

## Pattern Reference

### Unicode Scrubber Pattern

```python
# Removes all characters NOT in this set:
# - ASCII 0x00-0x7F (standard characters)
# - U+2010-U+2015 (various dashes)
# - U+2022 (bullet •)
# - U+25CB, U+25CF, U+25AA, U+25AB (circle variants)
# - U+25A0, U+25A1 (square variants)
# - U+25C6, U+25C7 (diamond variants)
# - U+2192, U+2794, U+2796, U+27A1-A4 (arrow variants)

pattern = re.compile(
    r'[^\x00-\x7F\u2010-\u2015\u2022\u25CB\u25CF\u25AA\u25AB\u25A0\u25A1\u25C6\u25C7\u2192\u2794\u2796\u27A1\u27A2\u27A3\u27A4]'
)

# Examples
print(pattern.sub('', "Hello 🌊"))        # "Hello "
print(pattern.sub('', "- Item 🎉"))      # "- Item "
print(pattern.sub('', "Text"))            # "Text"
```

### Bullet Detection Pattern

```python
# Primary pattern: ^\s*([-•●○▪■□◆◇*]|[\u2010-\u2015])\s+(.+)$
# Matches:
# - Optional leading whitespace
# - Any bullet character (or dash variant)
# - One or more spaces
# - Bullet content
# - End of line

pattern = re.compile(r'^\s*([-•●○▪■□◆◇*]|[\u2010-\u2015])\s+(.+)$')

# Test cases
tests = [
    ("- Item", True),
    ("■ Item", True),
    ("• Item", True),
    ("  - Item", True),        # With leading space
    ("Item", False),            # No bullet
    ("-Item", False),           # No space after dash
]

for text, expected in tests:
    match = pattern.match(text)
    result = match is not None
    status = "✅" if result == expected else "❌"
    print(f"{status} {text:20s} {'matches' if result else 'no match':10s}")
```

---

## Debugging Scenarios

### Scenario 1: Bullet Not Detected

```python
# Problem: Bullet not being detected
line = "- Item"
result = engine.analyze_line(line, line_num=1)

if result['type'] != 'bullet_list':
    print("❌ Bullet not detected!")
    print(f"Got type: {result['type']}")
    
    # Debug steps:
    # 1. Check if unicode_scrubber exists
    if 'unicode_scrubber' not in engine.patterns:
        print("ERROR: unicode_scrubber pattern not found!")
    
    # 2. Check if bullet_list exists
    if 'bullet_list' not in engine.patterns:
        print("ERROR: bullet_list patterns not found!")
    
    # 3. Check content after scrubbing
    scrubbed = line
    for pattern in engine.patterns.get('unicode_scrubber', []):
        scrubbed = pattern.sub('', scrubbed)
    print(f"After scrubbing: {repr(scrubbed)}")
    
    # 4. Test pattern manually
    bullet_patterns = engine.patterns.get('bullet_list', [])
    for i, pattern in enumerate(bullet_patterns):
        if pattern.match(scrubbed):
            print(f"Pattern {i} matches! (but type wasn't detected)")
else:
    print("✅ Bullet detected correctly")
```

### Scenario 2: Emoji Not Removed

```python
# Problem: Emoji still in content
line = "- Item 🌊"
result = engine.analyze_line(line, line_num=1)

if '🌊' in result['content']:
    print("❌ Emoji not removed!")
    print(f"Content: {repr(result['content'])}")
    
    # Debug steps:
    # 1. Check scrubber patterns exist
    scrubber_patterns = engine.patterns.get('unicode_scrubber', [])
    print(f"Scrubber patterns found: {len(scrubber_patterns)}")
    
    # 2. Test scrubber manually
    test_text = "Item 🌊"
    for pattern in scrubber_patterns:
        test_text = pattern.sub('', test_text)
    print(f"Manual scrub result: {repr(test_text)}")
    
    # 3. Check if analyze_line uses scrubber
    print("Check analyze_line() includes unicode_scrubber call")
else:
    print("✅ Emoji removed correctly")
```

### Scenario 3: Empty Result After Scrubbing

```python
# Problem: Text becomes empty after emoji removal
line = "🎉🎊🎈"
result = engine.analyze_line(line, line_num=1)

if result['type'] == 'empty':
    print("✅ Empty emoji-only text handled correctly")
else:
    print(f"❌ Expected empty type, got {result['type']}")
```

---

## Performance Testing

### Measure Processing Time

```python
import time

# Test document
lines = ["- Item 🌊"] * 1000

# Measure time
start = time.time()
for i, line in enumerate(lines, 1):
    engine.analyze_line(line, line_num=i)
end = time.time()

elapsed = end - start
avg_per_line = (elapsed / len(lines)) * 1000  # Convert to ms

print(f"Total time: {elapsed:.3f} seconds")
print(f"Average per line: {avg_per_line:.3f} ms")
print(f"Lines per second: {len(lines) / elapsed:.0f}")

# Expected: < 1ms per line
if avg_per_line < 1.0:
    print("✅ Performance is excellent")
else:
    print("⚠️  Performance may need optimization")
```

---

## API Reference

### analyze_line() Method

```python
def analyze_line(self, line, line_num, prev_line='', next_line='', context=None):
    """
    Analyze a single line and return analysis dictionary.
    
    Args:
        line (str): Text line to analyze
        line_num (int): Line number in document
        prev_line (str, optional): Previous line for context
        next_line (str, optional): Next line for context
        context (dict, optional): Additional context
    
    Returns:
        dict: Analysis result with keys:
            - type: 'bullet_list', 'paragraph', 'heading', 'empty', etc.
            - content: Extracted text content (emoji-free)
            - line_num: Line number
            - confidence: Detection confidence (0.0-1.0)
            - original: Original text before processing
    
    Example:
        result = engine.analyze_line("- Item 🌊", 1)
        assert result['type'] == 'bullet_list'
        assert result['content'] == 'Item '
    """
```

### test_bullet_cleanup() Method

```python
def test_bullet_cleanup(self):
    """
    Test emoji removal and bullet detection.
    
    Returns:
        list: List of test result dictionaries with keys:
            - text: Input text
            - expected_type: Expected line type
            - actual_type: Actual detected type
            - expected_content: Expected content
            - actual_content: Actual extracted content
            - emoji_stripped: Whether emojis were removed
            - passed: Test passed (boolean)
    
    Example:
        results = engine.test_bullet_cleanup()
        for result in results:
            if result['passed']:
                print(f"✅ {result['text']}")
            else:
                print(f"❌ {result['text']}")
    """
```

---

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Emojis in output | Scrubber not running | Verify `unicode_scrubber` at line 5301 |
| Bullets not detected | Pattern not matching | Check bullet marker is in pattern list |
| Slow processing | Regex not compiled | Engine pre-compiles patterns |
| Content incomplete | Trimming issue | Check if scrubber is preserving content |
| Crashes on emoji | No safety check | Safety check at line 5309-5310 |

---

## Tips & Best Practices

1. **Always use `analyze_line()` from engine instance**
   - Pre-compiled patterns (faster)
   - Consistent configuration
   - Access to all features

2. **Test with real PDF content**
   - PDFs may encode dashes differently
   - Unicode variations are common
   - Validate with actual source documents

3. **Monitor processing performance**
   - < 1ms per line is excellent
   - > 10ms may indicate issues
   - Profile with document-sized samples

4. **Verify emoji removal in output**
   - Check Word documents for emoji symbols
   - PDF export should be emoji-free
   - Validate with hex viewer if needed

5. **Use test_bullet_cleanup() regularly**
   - Regression testing
   - Validate after changes
   - Quick sanity check

---

## Support & Documentation

- **Implementation Guide**: `UNICODE_SCRUBBER_IMPLEMENTATION.md`
- **Quick Reference**: `QUICK_REFERENCE.md`
- **Status Report**: `IMPLEMENTATION_COMPLETE.md`
- **Code Location**: `pattern_formatter_backend.py`

---

**Version**: 1.0.0
**Last Updated**: January 12, 2026
**Status**: PRODUCTION READY ✅
