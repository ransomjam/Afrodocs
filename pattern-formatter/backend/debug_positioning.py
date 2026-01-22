"""Debug: Check what positioning properties are being saved before merge"""
from docx import Document

# Check the original standalone coverpage
doc = Document("c:\\Users\\user\\Desktop\\Afrodocs_dev\\Afrodocs\\pattern-formatter\\backend\\standalone_coverpage.docx")

print("Original Standalone Coverpage Properties:")
print("="*60)

for idx, para in enumerate(doc.paragraphs):
    if idx > 25:
        break
    
    if para.text.strip():
        pf = para.paragraph_format
        print(f"Para {idx}:")
        print(f"  text: {para.text[:50]}")
        print(f"  alignment: {para.alignment}")
        print(f"  space_before: {pf.space_before}")
        print(f"  space_after: {pf.space_after}")
        print(f"  left_indent: {pf.left_indent}")
        print(f"  first_line_indent: {pf.first_line_indent}")
        print(f"  line_spacing: {pf.line_spacing}")
        print()
