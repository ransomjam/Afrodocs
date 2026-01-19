"""Deep inspect dissertation templates - look for ALL placeholders"""
from docx import Document
from docx.oxml import parse_xml

templates = {
    'Bamenda': 'pattern-formatter/Cover Pages/Cover Pages _ University of Bamenda/Dissertation Cover Page Template.docx',
    'Buea': 'pattern-formatter/Cover Pages/Cover Page _ University of Buea/Dissertation Cover Page Template.docx'
}

for uni, path in templates.items():
    print(f"\n{'='*70}")
    print(f"{uni.upper()} - ALL PLACEHOLDERS & CONTENT")
    print(f"{'='*70}")
    
    doc = Document(path)
    
    # Get ALL text from all elements
    print("\nALL CONTENT (all paragraphs):")
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if text:
            # Check font
            fonts = set()
            for run in para.runs:
                fonts.add(run.font.name or 'DEFAULT')
            font_str = ', '.join(fonts)
            print(f"{i:2d}: [{font_str:20s}] {text[:80]}")
    
    # Check for shape textboxes (the hard way)
    print("\nLooking for shape textboxes in document part...")
    try:
        # Check document element for any shapes
        root = doc.element.getroottree().getroot()
        # Look for all text in shapes
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        }
        
        # Find all text boxes and their content
        found_shapes = False
        for elem in root.iter():
            if 'txbxContent' in str(elem.tag):
                found_shapes = True
                print("FOUND TEXTBOX CONTENT!")
                for t_elem in elem.iter():
                    if '}t' in str(t_elem.tag):  # Text element
                        if t_elem.text and ('{{' in t_elem.text or t_elem.text.strip()):
                            print(f"  Text: {repr(t_elem.text)}")
        
        if not found_shapes:
            print("No textbox elements found in document XML")
    except Exception as e:
        print(f"Error inspecting shapes: {e}")
