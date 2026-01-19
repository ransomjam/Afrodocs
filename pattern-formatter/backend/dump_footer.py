from docx import Document
import os

path = os.path.join('outputs','e7953ba8-99ca-49fd-9a55-784dbf149b4e_formatted.docx')
print('Checking', path)

doc = Document(path)
for si, section in enumerate(doc.sections):
    footer = section.footer
    print('\nSection', si)
    for pi, para in enumerate(footer.paragraphs):
        al = para.paragraph_format.alignment
        print(f' Para {pi}: align={al}, text={para.text!r}')
        for ri, run in enumerate(para.runs):
            rtxt = run.text
            fname = run.font.name
            fsize = run.font.size.pt if run.font.size else None
            color = None
            try:
                color = run.font.color.rgb
            except Exception:
                pass
            print(f'   Run {ri}: {rtxt!r}, font={fname}, size={fsize}, color={color}')
