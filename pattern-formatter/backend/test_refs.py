from pattern_formatter_backend import DocumentProcessor
fp = r'c:/Users/user/Desktop/Afrodocs_dev/Afrodocs/Samples/Jam _ sample project with figures.docx'
proc = DocumentProcessor()
with open(fp,'rb') as f:
    res = proc.process_docx(f)
# Unpack
if isinstance(res, tuple):
    result, images, shapes = res
else:
    result = res
structured = result.get('structured', []) if isinstance(result, dict) else []
refs = []

def walk(secs):
    for s in secs:
        if not isinstance(s, dict):
            continue
        if s.get('type') == 'section' and s.get('is_references_section'):
            refs.append(s)
        content = s.get('content', [])
        if isinstance(content, list):
            walk(content)

walk(structured)
print('Reference sections found:', len(refs))
for idx,sec in enumerate(refs):
    print('\n--- Reference Section', idx+1, 'Heading:', sec.get('heading'))
    count=0
    for item in sec.get('content', []):
        if isinstance(item, dict):
            itype = item.get('type')
            # try common keys
            text = item.get('text') or item.get('content') or item.get('original') or ''
            indent = item.get('indent')
            hanging = item.get('hanging')
            print(f"{count+1}. type={itype} indent={indent} hanging={hanging} text={str(text)[:200]}")
        else:
            print('Non-dict item:', str(item)[:200])
        count += 1
        if count >= 30:
            break
print('\nDone')
