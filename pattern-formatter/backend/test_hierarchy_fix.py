"""
Test script to verify the hierarchy preservation fixes.
"""
import sys
sys.path.insert(0, '.')

from pattern_formatter_backend import HeadingNumberer, DocumentProcessor

def test_extract_existing_number():
    """Test that extract_existing_number works for deep hierarchies."""
    hn = HeadingNumberer()
    
    test_cases = [
        ('1.1 Title', ('1.1', 'Title')),
        ('1.1.1 Title', ('1.1.1', 'Title')),
        ('1.1.1.1 Title', ('1.1.1.1', 'Title')),
        ('1.1.1.1.1 Deep Hierarchy', ('1.1.1.1.1', 'Deep Hierarchy')),
        ('1.2.3.4.5.6 Six Levels', ('1.2.3.4.5.6', 'Six Levels')),
        ('1.2.3.4.5.6.7.8.9.10 Ten Levels', ('1.2.3.4.5.6.7.8.9.10', 'Ten Levels')),
        ('A.1.2.3 Appendix', ('A.1.2.3', 'Appendix')),
        ('Research Objectives', (None, 'Research Objectives')),
    ]
    
    print("Testing extract_existing_number:")
    all_passed = True
    for text, expected in test_cases:
        result = hn.extract_existing_number(text)
        passed = result == expected
        status = "✓" if passed else "✗"
        print(f"  {status} '{text}' -> {result}")
        if not passed:
            print(f"      Expected: {expected}")
            all_passed = False
    
    return all_passed


def test_already_has_number():
    """Test that already_has_number recognizes deep hierarchies."""
    hn = HeadingNumberer()
    
    test_cases = [
        ('1.1 Title', True),
        ('1.1.1 Title', True),
        ('1.1.1.1 Title', True),
        ('1.1.1.1.1 Deep', True),
        ('1.2.3.4.5.6.7.8.9.10 Ten Levels', True),
        ('A.1.2.3 Appendix', True),
        ('1. Simple', True),
        ('Research Objectives', False),
        ('CHAPTER ONE', False),
    ]
    
    print("\nTesting already_has_number:")
    all_passed = True
    for text, expected in test_cases:
        result = hn.already_has_number(text)
        passed = result == expected
        status = "✓" if passed else "✗"
        print(f"  {status} '{text}' -> {result}")
        if not passed:
            print(f"      Expected: {expected}")
            all_passed = False
    
    return all_passed


def test_preserve_numbering():
    """Test that number_heading preserves existing numbers."""
    hn = HeadingNumberer()
    hn.current_chapter = 1  # Simulate being in Chapter 1
    
    test_cases = [
        '1.2 Research Objectives',
        '1.2.1 Main Research Objective',
        '1.2.2 Specific Research Objectives',
        '1.3 Research Questions',
        '1.3.1 Main Research Question',
        '1.3.1.1 Sub Question One',
        '1.3.1.2 Sub Question Two',
        '1.4.1.2.3.4.5 Deep Hierarchy',
    ]
    
    print("\nTesting number_heading preserves existing numbers:")
    all_passed = True
    for text in test_cases:
        result = hn.number_heading(text)
        original_num, _ = hn.extract_existing_number(text)
        preserved = result['number'] == original_num
        status = "✓" if preserved else "✗"
        print(f"  {status} '{text}' -> number: {result['number']}, was_renumbered: {result['was_renumbered']}")
        if not preserved:
            print(f"      Original: {original_num}")
            all_passed = False
    
    return all_passed


if __name__ == '__main__':
    print("=" * 60)
    print("Hierarchy Preservation Fix Tests")
    print("=" * 60)
    
    tests = [
        test_extract_existing_number,
        test_already_has_number,
        test_preserve_numbering,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"ERROR: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    if all(results):
        print("All tests PASSED! ✓")
    else:
        print("Some tests FAILED! ✗")
    print("=" * 60)
