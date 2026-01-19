from pattern_formatter_backend import DocumentProcessor

SAMPLE = """Below is a structured, academic-style treatment of the three themes—history of artificial intelligence, effects of AI on human intelligence, and human wisdom—with clear separation and logical flow.

---

## 1. History of Artificial Intelligence

Artificial Intelligence (AI) refers to the development of computer systems capable of performing tasks that traditionally require human intelligence, such as reasoning, learning, problem-solving, and decision-making.

### 1.1 Early Foundations (1940s–1950s)

* The conceptual roots of AI trace back to Alan Turing, who in 1950 proposed the Turing Test as a measure of machine intelligence.
* Early work focused on symbolic reasoning and mathematical logic.
* The term "Artificial Intelligence" was formally coined in 1956 at the Dartmouth Conference by John McCarthy.

### 1.2 Symbolic AI and Expert Systems (1960s–1980s)

* Researchers attempted to encode human knowledge into rule-based systems.
* Expert systems such as MYCIN were developed to mimic human decision-making in specific domains.
* Progress was limited by computing power and the difficulty of capturing human intuition.

### 1.3 AI Winters and Revival (1980s–2000s)

* Overpromising and underdelivering led to periods known as AI winters, where funding and interest declined.
* Revival occurred with improved hardware, access to large datasets, and better algorithms.

### 1.4 Modern AI and Machine Learning (2010–Present)

* Advances in machine learning, deep learning, and neural networks transformed AI capabilities.
* AI systems now excel in image recognition, language processing, autonomous systems, and data analysis.
* Current AI is narrow AI, meaning it performs specific tasks but lacks general human understanding.

---

## 2. Effects of AI on Human Intelligence

AI has both enhancing and challenging effects on human cognitive abilities.

### 2.1 Positive Effects

* Cognitive augmentation: AI assists humans in complex problem-solving, data analysis, and pattern recognition.
* Improved learning: Adaptive learning systems personalise education based on individual needs.
* Creativity support: AI tools support writing, design, music, and research by accelerating idea generation.
* Efficiency and accuracy: AI reduces human error in repetitive or data-heavy tasks.

### 2.2 Negative Effects

* Cognitive dependence: Over-reliance on AI may weaken critical thinking, memory, and problem-solving skills.
* Reduced deep thinking: Instant AI-generated answers can discourage reflection and intellectual struggle.
* Skill erosion: Certain skills may become obsolete as machines automate them.
* Bias reinforcement: AI systems may amplify human biases if trained on biased data.

### 2.3 Net Impact

AI does not inherently reduce human intelligence; rather, it reshapes how intelligence is exercised. The outcome depends on how humans choose to integrate AI into learning, work, and decision-making.

---

## 3. Human Wisdom in the Age of AI

### 3.1 Intelligence vs Wisdom

* Intelligence involves acquiring and applying knowledge efficiently.
* Wisdom involves judgment, ethics, empathy, and long-term understanding.
* AI can simulate intelligence but lacks consciousness, moral reasoning, and lived experience.

### 3.2 Role of Human Wisdom

* Ethical oversight: Humans must decide how AI is used, regulated, and controlled.
* Value-based decisions: Wisdom guides choices where data alone is insufficient.
* Contextual understanding: Humans interpret meaning, culture, and emotion beyond algorithmic output.
* Responsibility: Accountability for AI decisions ultimately rests with humans.

### 3.3 Coexistence of AI and Human Wisdom

* The future is not AI replacing humans but AI augmenting human wisdom.
* Wise use of AI requires critical thinking, ethical frameworks, and conscious limits.
* Education should prioritise reasoning, ethics, and creativity alongside technical skills.

---

## 4. Conclusion

Artificial Intelligence is a powerful technological evolution with deep historical roots. While it significantly influences human intelligence—both positively and negatively—it cannot replace human wisdom. The true challenge of the AI era is not building smarter machines, but cultivating wiser humans who can guide technology responsibly for societal benefit.

If you want this rewritten as an essay, presentation notes, or exam-ready answer, tell me the required format and length.
"""

proc = DocumentProcessor()
result, imgs = proc.process_text(SAMPLE)

analyzed = result.get('analyzed', [])
structured = result.get('structured', [])

print('Analyzed count:', len(analyzed))
print('Last 10 analyzed items:')
for a in analyzed[-10:]:
    print('-', a.get('type'), '|', a.get('content', a.get('text'))[:120])

print('\nStructured sections count:', len(structured))
print('Last section:')
if structured:
    last = structured[-1]
    print('  type:', last.get('type'))
    print('  heading:', last.get('heading') or last.get('title'))
    print('  content items:', len(last.get('content', [])))
    for c in last.get('content', [])[-3:]:
        print('   ', c.get('type'), c.get('text') if isinstance(c, dict) else str(c)[:120])
else:
    print('  none')
