#!/usr/bin/env python3
"""
Quick check of the most recent output file
"""

from docx import Document
import os
from pathlib import Path

# Get the most recent docx in outputs
outputs_dir = "./outputs"
files = list(Path(outputs_dir).glob("*_formatted.docx"))
latest = max(files, key=os.path.getctime)

print(f"Checking: {latest.name}")
print("="*70)

doc = Document(latest)

for idx, para in enumerate(doc.paragraphs[:5]):
    text_preview = para.text[:50] if para.text else "[EMPTY]"
    style_name = para.style.name if para.style else "None"
    line_spacing = para.paragraph_format.line_spacing
    
    print(f"\nPara {idx}: {style_name}")
    print(f"  Text: {text_preview}")
    print(f"  Line spacing: {line_spacing}")
    
    if para.runs:
        for run_idx, run in enumerate(para.runs[:1]):
            if run.font.size:
                print(f"  Run font size: {run.font.size.pt}pt")
            else:
                print(f"  Run font size: [inherited]")
