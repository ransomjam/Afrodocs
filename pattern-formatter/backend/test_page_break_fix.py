#!/usr/bin/env python3
"""Test to verify page breaks are removed for small documents"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pattern_formatter_backend import PatternEngine, DocumentProcessor, WordGenerator

# Sample text with markdown horizontal rules (---)
SAMPLE_TEXT = """Below is a structured, academic-style treatment of the three themes—**history of artificial intelligence**, **effects of AI on human intelligence**, and **human wisdom**—with clear separation and logical flow.

---

## 1. History of Artificial Intelligence

Artificial Intelligence (AI) refers to the development of computer systems capable of performing tasks that traditionally require human intelligence, such as reasoning, learning, problem-solving, and decision-making.

### 1.1 Early Foundations (1940s–1950s)

* The conceptual roots of AI trace back to **Alan Turing**, who in 1950 proposed the *Turing Test* as a measure of machine intelligence.
* Early work focused on symbolic reasoning and mathematical logic.
* The term **"Artificial Intelligence"** was formally coined in **1956** at the Dartmouth Conference by John McCarthy.

### 1.2 Symbolic AI and Expert Systems (1960s–1980s)

* Researchers attempted to encode human knowledge into rule-based systems.
* Expert systems such as **MYCIN** were developed to mimic human decision-making in specific domains.
* Progress was limited by computing power and the difficulty of capturing human intuition.

### 1.3 AI Winters and Revival (1980s–2000s)

* Overpromising and underdelivering led to periods known as **AI winters**, where funding and interest declined.
* Revival occurred with improved hardware, access to large datasets, and better algorithms.

### 1.4 Modern AI and Machine Learning (2010–Present)

* Advances in **machine learning**, **deep learning**, and **neural networks** transformed AI capabilities.
* AI systems now excel in image recognition, language processing, autonomous systems, and data analysis.
* Current AI is *narrow AI*, meaning it performs specific tasks but lacks general human understanding.

---

## 2. Effects of AI on Human Intelligence

AI has both **enhancing** and **challenging** effects on human cognitive abilities.

### 2.1 Positive Effects

* **Cognitive augmentation**: AI assists humans in complex problem-solving, data analysis, and pattern recognition.
* **Improved learning**: Adaptive learning systems personalise education based on individual needs.
* **Creativity support**: AI tools support writing, design, music, and research by accelerating idea generation.
* **Efficiency and accuracy**: AI reduces human error in repetitive or data-heavy tasks.

### 2.2 Negative Effects

* **Cognitive dependence**: Over-reliance on AI may weaken critical thinking, memory, and problem-solving skills.
* **Reduced deep thinking**: Instant AI-generated answers can discourage reflection and intellectual struggle.
* **Skill erosion**: Certain skills may become obsolete as machines automate them.
* **Bias reinforcement**: AI systems may amplify human biases if trained on biased data.

### 2.3 Net Impact

AI does not inherently reduce human intelligence; rather, it **reshapes how intelligence is exercised**. The outcome depends on how humans choose to integrate AI into learning, work, and decision-making.

---

## 3. Human Wisdom in the Age of AI

### 3.1 Intelligence vs Wisdom

* **Intelligence** involves acquiring and applying knowledge efficiently.
* **Wisdom** involves judgment, ethics, empathy, and long-term understanding.
* AI can simulate intelligence but lacks consciousness, moral reasoning, and lived experience.

### 3.2 Role of Human Wisdom

* **Ethical oversight**: Humans must decide how AI is used, regulated, and controlled.
* **Value-based decisions**: Wisdom guides choices where data alone is insufficient.
* **Contextual understanding**: Humans interpret meaning, culture, and emotion beyond algorithmic output.
* **Responsibility**: Accountability for AI decisions ultimately rests with humans.

### 3.3 Coexistence of AI and Human Wisdom

* The future is not AI replacing humans but **AI augmenting human wisdom**.
* Wise use of AI requires critical thinking, ethical frameworks, and conscious limits.
* Education should prioritise reasoning, ethics, and creativity alongside technical skills.

---

## 4. Conclusion

Artificial Intelligence is a powerful technological evolution with deep historical roots. While it significantly influences human intelligence—both positively and negatively—it cannot replace human wisdom. The true challenge of the AI era is not building smarter machines, but **cultivating wiser humans** who can guide technology responsibly for societal benefit.

If you want this rewritten as an **essay**, **presentation notes**, or **exam-ready answer**, tell me the required format and length.
"""

def test_pattern_detection():
    """Test that horizontal rules are detected correctly"""
    engine = PatternEngine()
    
    # Test horizontal rule detection
    test_lines = [
        "---",
        "***",
        "___",
        "[PAGE BREAK]",
        "\\newpage",
    ]
    
    print("=" * 60)
    print("PATTERN DETECTION TEST")
    print("=" * 60)
    
    for line in test_lines:
        analysis = engine.analyze_line(line, {})
        print(f"Line: '{line}' -> Type: {analysis.get('type', 'unknown')}")
    
    return True

def test_document_processing():
    """Test document processing with sample text"""
    processor = DocumentProcessor()
    
    print("\n" + "=" * 60)
    print("DOCUMENT PROCESSING TEST")
    print("=" * 60)
    
    # Process the text
    result, images = processor.process_text(SAMPLE_TEXT)
    
    # Count different types
    type_counts = {}
    page_break_lines = []
    horizontal_rule_lines = []
    
    for i, line in enumerate(result):
        line_type = line.get('type', 'unknown')
        type_counts[line_type] = type_counts.get(line_type, 0) + 1
        
        if line_type == 'page_break':
            page_break_lines.append((i, line.get('content', line.get('text', ''))))
        elif line_type == 'horizontal_rule':
            horizontal_rule_lines.append((i, line.get('content', line.get('text', ''))))
    
    print(f"\nTotal lines processed: {len(result)}")
    print(f"\nType distribution:")
    for t, count in sorted(type_counts.items()):
        print(f"  {t}: {count}")
    
    print(f"\nPage breaks found: {len(page_break_lines)}")
    for idx, content in page_break_lines:
        print(f"  Line {idx}: '{content}'")
    
    print(f"\nHorizontal rules found: {len(horizontal_rule_lines)}")
    for idx, content in horizontal_rule_lines:
        print(f"  Line {idx}: '{content}'")
    
    return page_break_lines, horizontal_rule_lines

def test_word_generation():
    """Test Word document generation"""
    processor = DocumentProcessor()
    generator = WordGenerator()
    
    print("\n" + "=" * 60)
    print("WORD GENERATION TEST")
    print("=" * 60)
    
    # Process the text
    result, images = processor.process_text(SAMPLE_TEXT)
    
    # Structure the content (simulate what happens in the upload route)
    from pattern_formatter_backend import structure_analyzed_content
    structured = structure_analyzed_content(result)
    
    print(f"\nStructured sections: {len(structured)}")
    
    # Calculate document size metrics
    total_chars = 0
    for s in structured:
        if isinstance(s, dict):
            total_chars += len(str(s.get('heading', '')))
            content = s.get('content', [])
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict):
                        total_chars += len(str(c.get('text', '')))
    
    estimated_pages = total_chars / 2000
    section_count = len(structured)
    is_short = estimated_pages < 5 or section_count < 5
    
    print(f"Total chars: {total_chars}")
    print(f"Estimated pages: {estimated_pages:.1f}")
    print(f"Section count: {section_count}")
    print(f"Is short document: {is_short}")
    
    # Check sections for page break flags
    print("\nSection page break flags:")
    for i, s in enumerate(structured):
        if isinstance(s, dict):
            heading = s.get('heading', s.get('title', 'No heading'))[:50]
            npb = s.get('needs_page_break', False)
            sonp = s.get('start_on_new_page', False)
            upbb = s.get('use_page_break_before', False)
            print(f"  [{i}] '{heading}...' -> needs_page_break={npb}, start_on_new_page={sonp}, use_page_break_before={upbb}")
            
            # Check content items for page_break type
            for j, item in enumerate(s.get('content', [])):
                if isinstance(item, dict) and item.get('type') == 'page_break':
                    print(f"      Content [{j}]: page_break item found!")
                elif isinstance(item, dict) and item.get('type') == 'horizontal_rule':
                    print(f"      Content [{j}]: horizontal_rule item found")
    
    # Generate output
    output_path = os.path.join(os.path.dirname(__file__), 'test_no_breaks_output.docx')
    generator.generate(structured, output_path, images=[])
    
    print(f"\nGenerated document: {output_path}")
    print(f"Generator is_short_document flag: {generator.is_short_document}")
    
    return output_path

if __name__ == '__main__':
    print("Testing Page Break Fix")
    print("=" * 60)
    
    test_pattern_detection()
    page_breaks, horiz_rules = test_document_processing()
    output = test_word_generation()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if len(page_breaks) == 0:
        print("✓ No page_break types detected - horizontal rules correctly classified!")
    else:
        print(f"✗ {len(page_breaks)} page_break types still detected - FIX NEEDED")
    
    print(f"\nOutput file: {output}")
    print("Please open the output file to verify no page breaks exist.")
