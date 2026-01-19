#!/usr/bin/env python3
"""
Simple test to identify page break issue in small documents
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import DocumentProcessor, PatternEngine

def test_small_document():
    """Test processing a small document to identify page break issues"""
    
    # Small document content with horizontal rules
    content = """Below is a structured, academic-style treatment of the three themes—**history of artificial intelligence**, **effects of AI on human intelligence**, and **human wisdom**—with clear separation and logical flow.

---

## 1. History of Artificial Intelligence

Artificial Intelligence (AI) refers to the development of computer systems capable of performing tasks that traditionally require human intelligence, such as reasoning, learning, problem-solving, and decision-making.

### 1.1 Early Foundations (1940s–1950s)

* The conceptual roots of AI trace back to **Alan Turing**, who in 1950 proposed the *Turing Test* as a measure of machine intelligence.
* Early work focused on symbolic reasoning and mathematical logic.
* The term **"Artificial Intelligence"** was formally coined in **1956** at the Dartmouth Conference by John McCarthy.

---

## 2. Effects of AI on Human Intelligence

AI has both **enhancing** and **challenging** effects on human cognitive abilities.

### 2.1 Positive Effects

* **Cognitive augmentation**: AI assists humans in complex problem-solving, data analysis, and pattern recognition.
* **Improved learning**: Adaptive learning systems personalise education based on individual needs.
* **Creativity support**: AI tools support writing, design, music, and research by accelerating idea generation.
* **Efficiency and accuracy**: AI reduces human error in repetitive or data-heavy tasks.

---

## 3. Human Wisdom in the Age of AI

### 3.1 Intelligence vs Wisdom

* **Intelligence** involves acquiring and applying knowledge efficiently.
* **Wisdom** involves judgment, ethics, empathy, and long-term understanding.
* AI can simulate intelligence but lacks consciousness, moral reasoning, and lived experience.

## 4. Conclusion

Artificial Intelligence is a powerful technological evolution with deep historical roots. While it significantly influences human intelligence—both positively and negatively—it cannot replace human wisdom."""

    print("Testing small document processing...")
    print("=" * 50)
    print(f"Content length: {len(content)} characters")
    print(f"Word count: {len(content.split())} words")
    print("=" * 50)
    
    try:
        # Initialize the processor
        processor = DocumentProcessor()
        
        # Check if it's detected as a short document
        pattern_engine = PatternEngine()
        is_short, reason = pattern_engine.is_short_document(content)
        print(f"Is short document: {is_short}")
        print(f"Reason: {reason}")
        print("=" * 50)
        
        # Process the content
        result, images = processor.process_text(content)
        
        print(f"Processing result type: {type(result)}")
        print(f"Number of items: {len(result) if hasattr(result, '__len__') else 'N/A'}")
        print(f"Images: {len(images) if images else 0}")
        
        # Analyze the result
        print(f"\nResult structure: {type(result)}")
        if isinstance(result, dict):
            print("Result keys:", list(result.keys()))
            for key, value in result.items():
                print(f"  {key}: {type(value)} (len={len(value) if hasattr(value, '__len__') else 'N/A'})")
                if key == 'structured' and isinstance(value, list):
                    print("    Structured sections:")
                    for i, section in enumerate(value):  # Show all sections
                        if isinstance(section, dict):
                            heading = section.get('heading', section.get('title', 'No heading'))[:40]
                            content_len = len(section.get('content', []))
                            needs_break = section.get('needs_page_break', False)
                            start_new_page = section.get('start_on_new_page', False)
                            use_page_break = section.get('use_page_break_before', False)
                            print(f"      [{i}] '{heading}...' (content: {content_len} items)")
                            print(f"          needs_page_break: {needs_break}")
                            print(f"          start_on_new_page: {start_new_page}")
                            print(f"          use_page_break_before: {use_page_break}")
                            
                            # Check content for page breaks
                            content = section.get('content', [])
                            for j, item in enumerate(content):
                                if isinstance(item, dict):
                                    item_type = item.get('type', 'unknown')
                                    if 'page' in item_type or 'break' in item_type:
                                        print(f"            Content[{j}]: {item_type} - {item.get('text', item.get('content', ''))}")
                elif key == 'stats' and isinstance(value, dict):
                    print("    Stats:")
                    for stat_key, stat_value in value.items():
                        if 'short' in stat_key.lower() or 'page' in stat_key.lower():
                            print(f"      {stat_key}: {stat_value}")
        elif isinstance(result, list):
            print("\nAnalyzing processed lines:")
            for i, item in enumerate(result[:20]):  # Show first 20 items
                if isinstance(item, dict):
                    item_type = item.get('type', 'unknown')
                    content_preview = str(item.get('content', item.get('text', '')))[:50]
                    print(f"  [{i:2d}] {item_type:15s} | {content_preview}")
                else:
                    print(f"  [{i:2d}] {type(item).__name__:15s} | {str(item)[:50]}")
        
        print("=" * 50)
        print("Test completed successfully!")
        
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_small_document()