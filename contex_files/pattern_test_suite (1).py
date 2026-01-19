# test_pattern_formatter.py
# Comprehensive test suite for pattern-based document formatter

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from pattern_formatter_backend import PatternEngine, DocumentProcessor, WordGenerator


class ColorPrint:
    """Colored output for terminal"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    @staticmethod
    def success(msg):
        print(f"{ColorPrint.GREEN}✓{ColorPrint.END} {msg}")
    
    @staticmethod
    def error(msg):
        print(f"{ColorPrint.RED}✗{ColorPrint.END} {msg}")
    
    @staticmethod
    def info(msg):
        print(f"{ColorPrint.BLUE}ℹ{ColorPrint.END} {msg}")
    
    @staticmethod
    def header(msg):
        print(f"\n{ColorPrint.BOLD}{ColorPrint.BLUE}{msg}{ColorPrint.END}")
        print("=" * 60)


class TestPatternEngine:
    """Test pattern recognition engine"""
    
    def __init__(self):
        self.engine = PatternEngine()
        self.passed = 0
        self.failed = 0
    
    def test_heading_detection(self):
        """Test heading pattern matching"""
        ColorPrint.header("TEST 1: Heading Detection")
        
        test_cases = [
            # (line, expected_type, expected_level)
            ("INTRODUCTION", "heading", 1),
            ("Introduction and Background", "heading", 2),
            ("1.1 Overview", "heading", 2),
            ("1.1.1 Details", "heading", 3),
            ("CHAPTER 1: FOUNDATIONS", "heading", 1),
            ("Methods and Results", "heading", 2),
            ("This is a normal paragraph.", "paragraph", 0),
        ]
        
        for line, expected_type, expected_level in test_cases:
            result = self.engine.analyze_line(line, 0)
            
            if result['type'] == expected_type and result.get('level', 0) == expected_level:
                ColorPrint.success(f"'{line}' → {expected_type} L{expected_level}")
                self.passed += 1
            else:
                ColorPrint.error(f"'{line}' → Got {result['type']} L{result.get('level', 0)}, expected {expected_type} L{expected_level}")
                self.failed += 1
    
    def test_reference_detection(self):
        """Test reference pattern matching"""
        ColorPrint.header("TEST 2: Reference Detection")
        
        test_cases = [
            "Smith, J. (2024). Title of paper. Journal Name.",
            "Johnson et al. 2023. Research findings.",
            "[1] Author, I. (2024). Book title. Publisher.",
            "Brown, A. Retrieved from https://example.com",
        ]
        
        for line in test_cases:
            result = self.engine.analyze_line(line, 0)
            
            if result['type'] == 'reference':
                ColorPrint.success(f"Reference detected: {line[:50]}...")
                self.passed += 1
            else:
                ColorPrint.error(f"Failed to detect reference: {line[:50]}...")
                self.failed += 1
    
    def test_list_detection(self):
        """Test list pattern matching"""
        ColorPrint.header("TEST 3: List Detection")
        
        test_cases = [
            ("• First bullet point", "bullet_list"),
            ("- Second bullet point", "bullet_list"),
            ("* Third bullet point", "bullet_list"),
            ("1. First numbered item", "numbered_list"),
            ("a) Lettered item", "numbered_list"),
            ("i) Roman numeral item", "numbered_list"),
        ]
        
        for line, expected_type in test_cases:
            result = self.engine.analyze_line(line, 0)
            
            if result['type'] == expected_type:
                ColorPrint.success(f"'{line}' → {expected_type}")
                self.passed += 1
            else:
                ColorPrint.error(f"'{line}' → Got {result['type']}, expected {expected_type}")
                self.failed += 1
    
    def test_definition_detection(self):
        """Test definition pattern matching"""
        ColorPrint.header("TEST 4: Definition Detection")
        
        test_cases = [
            "Definition: A clear explanation of a term.",
            "Objective: The main goal of the research.",
            "Method: The approach used in the study.",
            "Conclusion: Final remarks and findings.",
        ]
        
        for line in test_cases:
            result = self.engine.analyze_line(line, 0)
            
            if result['type'] == 'definition':
                ColorPrint.success(f"Definition: {result.get('term', 'N/A')}")
                self.passed += 1
            else:
                ColorPrint.error(f"Failed to detect definition in: {line}")
                self.failed += 1
    
    def test_table_detection(self):
        """Test table pattern matching"""
        ColorPrint.header("TEST 5: Table Detection")
        
        test_cases = [
            ("[TABLE START]", "table_start"),
            ("Table 1: Sample data", "table_caption"),
            ("| Header 1 | Header 2 | Header 3 |", "table_row"),
            ("[TABLE END]", "table_end"),
        ]
        
        for line, expected_type in test_cases:
            result = self.engine.analyze_line(line, 0)
            
            if result['type'] == expected_type:
                ColorPrint.success(f"'{line}' → {expected_type}")
                self.passed += 1
            else:
                ColorPrint.error(f"'{line}' → Got {result['type']}, expected {expected_type}")
                self.failed += 1
    
    def run_all_tests(self):
        """Run all pattern tests"""
        ColorPrint.header("🧪 PATTERN ENGINE TEST SUITE")
        
        self.test_heading_detection()
        self.test_reference_detection()
        self.test_list_detection()
        self.test_definition_detection()
        self.test_table_detection()
        
        # Print summary
        ColorPrint.header("TEST SUMMARY")
        total = self.passed + self.failed
        percentage = (self.passed / total * 100) if total > 0 else 0
        
        print(f"Total Tests: {total}")
        print(f"Passed: {ColorPrint.GREEN}{self.passed}{ColorPrint.END}")
        print(f"Failed: {ColorPrint.RED}{self.failed}{ColorPrint.END}")
        print(f"Success Rate: {ColorPrint.BOLD}{percentage:.1f}%{ColorPrint.END}")
        
        return self.failed == 0


class TestDocumentProcessor:
    """Test document processing"""
    
    def __init__(self):
        self.processor = DocumentProcessor()
    
    def test_sample_document(self):
        """Test processing a complete sample document"""
        ColorPrint.header("TEST 6: Document Processing")
        
        sample_doc = """
INTRODUCTION

Background and Motivation

Cloud computing has revolutionized enterprise IT infrastructure. The following points highlight key advantages:

• Cost efficiency through shared resources
• Scalability on demand
• Global infrastructure access
- Reduced maintenance overhead

Definition: Cloud computing refers to on-demand delivery of computing resources over the internet.

1.1 Economies of Scale

Major providers achieve cost advantages through:

1. Bulk purchasing power
2. Operational efficiency
3. Automated management

REFERENCES

Smith, J. (2024). Cloud Economics. Tech Journal.
Johnson, A. et al. 2023. Scaling strategies.
Brown, M. Retrieved from https://cloudresearch.org
"""
        
        ColorPrint.info("Processing sample document...")
        result = self.processor.process_text(sample_doc)
        
        stats = result['stats']
        structured = result['structured']
        
        # Validate results
        tests = [
            (stats['headings'] >= 2, f"Headings detected: {stats['headings']}"),
            (stats['paragraphs'] >= 3, f"Paragraphs detected: {stats['paragraphs']}"),
            (stats['references'] >= 3, f"References detected: {stats['references']}"),
            (stats['lists'] >= 2, f"Lists detected: {stats['lists']}"),
            (stats['definitions'] >= 1, f"Definitions detected: {stats['definitions']}"),
            (len(structured) >= 2, f"Sections structured: {len(structured)}"),
        ]
        
        passed = 0
        failed = 0
        
        for test, msg in tests:
            if test:
                ColorPrint.success(msg)
                passed += 1
            else:
                ColorPrint.error(msg)
                failed += 1
        
        # Show structure
        ColorPrint.info("\nDocument Structure:")
        for section in structured:
            print(f"  {section['level']}. {section['heading']} ({len(section['content'])} items)")
        
        return failed == 0
    
    def test_edge_cases(self):
        """Test edge cases and unusual patterns"""
        ColorPrint.header("TEST 7: Edge Cases")
        
        edge_cases = [
            # Empty lines
            ("", "empty"),
            ("   ", "empty"),
            ("\n\n", "empty"),
            
            # Mixed case headings
            ("MiXeD CaSe HeAdInG", "paragraph"),  # Should be paragraph
            
            # Very long lines
            ("This is a very long paragraph that exceeds the typical length of a heading and should be classified as a regular paragraph rather than a heading even though it might start with a capital letter." * 5, "paragraph"),
            
            # Numbers only
            ("123456", "paragraph"),
            
            # Special characters
            ("@#$%^&*()", "paragraph"),
        ]
        
        passed = 0
        failed = 0
        
        for line, expected_type in edge_cases:
            result = self.processor.engine.analyze_line(line, 0)
            
            if result['type'] == expected_type:
                ColorPrint.success(f"Edge case handled: '{line[:30]}...' → {expected_type}")
                passed += 1
            else:
                ColorPrint.error(f"Edge case failed: '{line[:30]}...' → Got {result['type']}, expected {expected_type}")
                failed += 1
        
        return failed == 0


class TestPerformance:
    """Test system performance"""
    
    def __init__(self):
        self.processor = DocumentProcessor()
    
    def test_speed(self):
        """Test processing speed"""
        ColorPrint.header("TEST 8: Performance Benchmarks")
        
        import time
        
        # Generate test documents of various sizes
        test_sizes = [
            (100, "Small (100 lines)"),
            (1000, "Medium (1,000 lines)"),
            (5000, "Large (5,000 lines)"),
        ]
        
        for line_count, label in test_sizes:
            # Generate document
            lines = []
            for i in range(line_count):
                if i % 20 == 0:
                    lines.append(f"SECTION {i // 20}")
                elif i % 10 == 0:
                    lines.append(f"Subsection {i // 10}")
                else:
                    lines.append(f"This is paragraph number {i} with some sample text content.")
            
            doc_text = "\n".join(lines)
            
            # Measure processing time
            start_time = time.time()
            result = self.processor.process_text(doc_text)
            elapsed = time.time() - start_time
            
            lines_per_second = line_count / elapsed
            
            ColorPrint.success(f"{label}: {elapsed:.2f}s ({lines_per_second:.0f} lines/sec)")
        
        return True


def run_comprehensive_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print(f"{ColorPrint.BOLD}{ColorPrint.BLUE}PATTERN-BASED DOCUMENT FORMATTER")
    print(f"COMPREHENSIVE TEST SUITE{ColorPrint.END}")
    print("=" * 60)
    
    all_passed = True
    
    # Test 1-5: Pattern Engine
    pattern_tests = TestPatternEngine()
    all_passed &= pattern_tests.run_all_tests()
    
    # Test 6-7: Document Processor
    processor_tests = TestDocumentProcessor()
    all_passed &= processor_tests.test_sample_document()
    all_passed &= processor_tests.test_edge_cases()
    
    # Test 8: Performance
    performance_tests = TestPerformance()
    all_passed &= performance_tests.test_speed()
    
    # Final summary
    print("\n" + "=" * 60)
    if all_passed:
        print(f"{ColorPrint.GREEN}{ColorPrint.BOLD}✓ ALL TESTS PASSED{ColorPrint.END}")
        print(f"{ColorPrint.GREEN}System is ready for production use!{ColorPrint.END}")
    else:
        print(f"{ColorPrint.RED}{ColorPrint.BOLD}✗ SOME TESTS FAILED{ColorPrint.END}")
        print(f"{ColorPrint.YELLOW}Please review failures above{ColorPrint.END}")
    print("=" * 60 + "\n")
    
    return all_passed


def run_interactive_test():
    """Interactive test mode"""
    ColorPrint.header("INTERACTIVE TEST MODE")
    print("Enter text to analyze (or 'quit' to exit):\n")
    
    engine = PatternEngine()
    
    while True:
        try:
            line = input(f"{ColorPrint.BLUE}> {ColorPrint.END}")
            
            if line.lower() in ['quit', 'exit', 'q']:
                break
            
            if not line.strip():
                continue
            
            result = engine.analyze_line(line, 0)
            
            print(f"\n  Type: {ColorPrint.BOLD}{result['type']}{ColorPrint.END}")
            if result.get('level'):
                print(f"  Level: {result['level']}")
            print(f"  Confidence: {result['confidence']*100:.0f}%")
            print(f"  Content: {result['content'][:100]}")
            print()
            
        except KeyboardInterrupt:
            break
    
    ColorPrint.info("Exiting interactive mode...")


def create_sample_documents():
    """Create sample test documents"""
    ColorPrint.header("CREATING SAMPLE DOCUMENTS")
    
    # Sample 1: Academic Paper
    academic_sample = """
CLOUD COMPUTING AND ECONOMIES OF SCALE

ABSTRACT

This paper examines the economic principles underlying cloud computing infrastructure.

INTRODUCTION

Background and Context

Cloud computing has transformed enterprise IT delivery models. Key innovations include:

• Infrastructure as a Service (IaaS)
• Platform as a Service (PaaS)
• Software as a Service (SaaS)

Definition: Cloud computing refers to on-demand delivery of computing resources over the internet.

1.1 Economies of Scale

Three primary mechanisms drive cost advantages:

1. Resource consolidation
2. Bulk purchasing power
3. Operational automation

METHODOLOGY

Research Approach

This study employed a mixed-methods approach combining:

a) Quantitative analysis of pricing data
b) Qualitative interviews with cloud architects
c) Case study analysis

RESULTS

Key Findings

Table 1: Cost Comparison

| Provider | Cost/Hour | Discount |
| AWS | $0.10 | 30% |
| Azure | $0.09 | 25% |
| GCP | $0.08 | 35% |

DISCUSSION

The data reveals significant cost advantages at scale.

CONCLUSION

Cloud computing delivers measurable economic benefits through economies of scale.

REFERENCES

Smith, J. (2024). Cloud Economics. Tech Journal.
Johnson, A. et al. 2023. Scaling strategies.
Brown, M. Retrieved from https://cloudresearch.org
"""
    
    # Save sample
    with open('sample_academic_paper.txt', 'w', encoding='utf-8') as f:
        f.write(academic_sample)
    
    ColorPrint.success("Created: sample_academic_paper.txt")
    
    # Sample 2: Business Report
    business_sample = """
QUARTERLY BUSINESS REPORT

EXECUTIVE SUMMARY

Q4 2024 exceeded expectations with 15% revenue growth.

FINANCIAL PERFORMANCE

Revenue Breakdown

The company achieved the following results:

1. Product sales: $5M (up 20%)
2. Services: $3M (up 10%)
3. Subscriptions: $2M (up 25%)

Objective: Maintain growth trajectory in 2025.

MARKET ANALYSIS

Key trends observed:

- Digital transformation acceleration
- Increased cloud adoption
- Remote work sustainability

RECOMMENDATIONS

Strategic Initiatives

Priority actions for Q1 2025:

1) Expand product portfolio
2) Enhance customer support
3) Invest in R&D

CONCLUSION

Strong foundation established for continued growth.
"""
    
    with open('sample_business_report.txt', 'w', encoding='utf-8') as f:
        f.write(business_sample)
    
    ColorPrint.success("Created: sample_business_report.txt")
    
    ColorPrint.info("\nUse these samples to test the formatter!")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'interactive':
            run_interactive_test()
        elif sys.argv[1] == 'samples':
            create_sample_documents()
        else:
            print("Usage:")
            print("  python test_pattern_formatter.py           # Run all tests")
            print("  python test_pattern_formatter.py interactive # Interactive mode")
            print("  python test_pattern_formatter.py samples     # Create samples")
    else:
        success = run_comprehensive_tests()
        sys.exit(0 if success else 1)
