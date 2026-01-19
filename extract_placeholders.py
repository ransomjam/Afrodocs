import re
from docx import Document
import os

def extract_placeholders(doc_path):
    """Extract all {{}} placeholders from a Word document."""
    try:
        doc = Document(doc_path)
        placeholders = set()
        
        # Extract from paragraphs
        for paragraph in doc.paragraphs:
            matches = re.findall(r'\{\{([^}]+)\}\}', paragraph.text)
            placeholders.update(matches)
        
        # Extract from textboxes
        for rel in doc.part.rels.values():
            if "hyperlink" not in rel.target_ref:
                try:
                    shape = rel.target_part.element
                    for elem in shape.iter():
                        if elem.text:
                            matches = re.findall(r'\{\{([^}]+)\}\}', elem.text)
                            placeholders.update(matches)
                except:
                    pass
        
        return sorted(list(placeholders))
    except Exception as e:
        print(f"Error reading {doc_path}: {e}")
        return []

# Bamenda templates
bamenda_folder = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages\Cover Pages _ University of Bamenda"
buea_folder = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages\Cover Page _ University of Buea"

print("=" * 80)
print("BAMENDA TEMPLATES")
print("=" * 80)

for template in sorted(os.listdir(bamenda_folder)):
    if template.endswith(".docx") and "Template" in template:
        path = os.path.join(bamenda_folder, template)
        placeholders = extract_placeholders(path)
        print(f"\n{template}:")
        for p in placeholders:
            print(f"  {{{{ {p} }}}}")

print("\n" + "=" * 80)
print("BUEA TEMPLATES")
print("=" * 80)

for template in sorted(os.listdir(buea_folder)):
    if template.endswith(".docx") and "Template" in template:
        path = os.path.join(buea_folder, template)
        placeholders = extract_placeholders(path)
        print(f"\n{template}:")
        for p in placeholders:
            print(f"  {{{{ {p} }}}}")
