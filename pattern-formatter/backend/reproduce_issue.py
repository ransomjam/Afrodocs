
from pattern_formatter_backend import DocumentProcessor, PatternEngine, WordGenerator
import os

def reproduce_issue():
    print("Initializing Processor...")
    processor = DocumentProcessor()
    generator = WordGenerator()
    
    # Test Case: "Just a blanc sheet"
    # This might happen if the input is interpreted as empty or filtered out completely.
    
    # Scenario 1: Text with only AI meta-commentary (should be empty)
    print("\n--- Scenario 1: Only AI Meta-Commentary ---")
    text1 = "Here is the document you requested:\n\nHope this helps!"
    result1, _ = processor.process_text(text1)
    print(f"Structured sections: {len(result1.get('structured', []))}")
    print(f"Analyzed lines: {len(result1.get('analyzed', []))}")
    
    # Scenario 2: Text with weird spacing/newlines (simulating paste issues)
    print("\n--- Scenario 2: Weird Spacing ---")
    text2 = "   \n\n  Title  \n\n   Body text with   weird   spacing .  \n\n"
    result2, _ = processor.process_text(text2)
    print(f"Structured sections: {len(result2.get('structured', []))}")
    print(f"Analyzed lines: {len(result2.get('analyzed', []))}")
    
    # Scenario 3: Short document that might trigger TOC removal incorrectly
    print("\n--- Scenario 3: Short Doc / TOC Trigger ---")
    text3 = "Table of Contents\n\n1. Intro.....1\n\nIntroduction\n\nReal content."
    result3, _ = processor.process_text(text3)
    print(f"Structured sections: {len(result3.get('structured', []))}")
    print(f"Analyzed lines: {len(result3.get('analyzed', []))}")
    
    # Scenario 4: The "Blank Sheet" - maybe single line input?
    print("\n--- Scenario 4: Single Line Input ---")
    text4 = "This is a single line document."
    result4, _ = processor.process_text(text4)
    print(f"Structured sections: {len(result4.get('structured', []))}")
    print(f"Analyzed lines: {len(result4.get('analyzed', []))}")
    
    # Scenario 5: Input with \r only (Mac/Old formatting)
    print("\n--- Scenario 5: CR only ---")
    text5 = "Line 1\rLine 2\rLine 3"
    result5, _ = processor.process_text(text5)
    print(f"Structured sections: {len(result5.get('structured', []))}")
    print(f"Analyzed lines: {len(result5.get('analyzed', []))}")

    # Scenario 6: Input that looks like AI but is long
    print("\n--- Scenario 6: Long AI-like text ---")
    text6 = "Here is the document:\n" + "Content " * 50
    result6, _ = processor.process_text(text6)
    print(f"Structured sections: {len(result6.get('structured', []))}")
    print(f"Analyzed lines: {len(result6.get('analyzed', []))}")

if __name__ == "__main__":
    try:
        reproduce_issue()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
