from pattern_formatter_backend import DocumentProcessor, WordGenerator
import os
from docx import Document

SAMPLE = """Short doc for watermark test.

Hello world.
"""

proc = DocumentProcessor()
res, imgs = proc.process_text(SAMPLE)
structured = res.get('structured', [])

out = os.path.join(os.path.dirname(__file__), 'outputs', 'watermark_test.docx')
wg = WordGenerator()
wg.generate(structured, out, images=[], is_free_tier=True)

print('Generated', out)

# Inspect footer
doc = Document(out)
for i, section in enumerate(doc.sections):
    footer = section.footer
    for j, para in enumerate(footer.paragraphs):
        text = para.text
        try:
            align = para.paragraph_format.alignment
        except Exception:
            align = None
        print(f'Section {i} footer para {j!s}: align={align}, text={text!r}')
