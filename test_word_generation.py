#!/usr/bin/env python3
"""
Test Word generation to identify page break issue
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

from pattern_formatter_backend import DocumentProcessor, WordGenerator

def test_word_generation():
    """Test Word document generation for small document"""
    
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

    print("Testing Word generation for small document...")
    print("=" * 50)
    
    try:
        # Process the content
        processor = DocumentProcessor()
        result, images = processor.process_text(content)
        
        # Get structured data
        structured = result['structured']
        stats = result['stats']
        
        print(f"Document stats:")
        for key, value in stats.items():
            if 'short' in key.lower() or 'page' in key.lower() or 'word' in key.lower():
                print(f"  {key}: {value}")
        
        print(f"\nStructured sections: {len(structured)}")
        
        # Generate Word document
        generator = WordGenerator()
        output_path = os.path.join(os.path.dirname(__file__), 'test_small_doc_output.docx')
        
        print(f"\nGenerating Word document...")
        print(f"Output path: {output_path}")
        
        # Check if WordGenerator has short document detection
        print(f"WordGenerator attributes: {[attr for attr in dir(generator) if 'short' in attr.lower()]}")
        
        # Generate the document
        generator.generate(structured, output_path, images=[])
        
        print(f"\nDocument generated successfully!")
        print(f"File exists: {os.path.exists(output_path)}")
        
        # Check if WordGenerator set any flags
        if hasattr(generator, 'is_short_document'):
            print(f"WordGenerator.is_short_document: {generator.is_short_document}")
        
        return output_path
        
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_word_generation()