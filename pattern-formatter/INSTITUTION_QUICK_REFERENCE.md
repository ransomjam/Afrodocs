# Quick Reference: Adding Institutions

**TL;DR** - Steps to add a new institution

## 5-Minute Setup

### 1. File Structure
```
pattern-formatter/Cover Pages/
├── Cover Pages _ University of Bamenda/
│   ├── Assignments Cover Page Template.docx
│   ├── Dissertation Cover Page Template.docx
│   ├── Internship Cover Page Template.docx
│   └── Research Proposal Cover Page Template.docx
├── Cover Page _ University of Buea/          ← Note: "Page" singular
├── Cover Pages _ National University Institute (NPUI)/
├── Cover Page _ BUST/                        ← NEW
├── Cover Page _ Catholic University/         ← NEW
└── Cover Pages _ [NEW INSTITUTION NAME]/     ← Create this folder (when adding next)
    ├── Assignments Cover Page Template.docx
    ├── Dissertation Cover Page Template.docx
    ├── Internship Cover Page Template.docx
    └── Research Proposal Cover Page Template.docx
```

### 2. Update Backend Code

**File:** `pattern-formatter/backend/coverpage_generator.py` (Line ~51)

```python
institution_mapping = {
    'uba': 'Cover Pages _ University of Bamenda',
    'ub': 'Cover Page _ University of Buea',
    'npui': 'Cover Pages _ National University Institute (NPUI)',
    'bust': 'Cover Page _ BUST',                          # ← ADDED
    'cucb': 'Cover Page _ Catholic University',           # ← ADDED
    'NEW_ID': 'Cover Pages _ [NEW INSTITUTION NAME]',     # ← For future institutions
}
```

**CRITICAL:** Copy folder name EXACTLY from disk - watch for spaces!

### 3. Add Institution Data

**File:** `pattern-formatter/backend/data/institutions.json`

```json
{
  "id": "NEW_ID",
  "name": "New Institution Name",
  "short": "NIN",
  "logo": "nin_logo.png",
  "faculties": [
    {
      "name": "Faculty/School Name",
      "departments": ["Dept 1", "Dept 2", ...]
    }
  ]
}
```

### 4. Test
```bash
# Restart backend
cd pattern-formatter/backend
py pattern_formatter_backend.py

# Test API
curl -X POST http://localhost:5000/api/coverpage/generate \
  -H "Content-Type: application/json" \
  -d '{
    "institution":"NEW_ID",
    "faculty":"Faculty Name",
    "department":"Dept 1",
    "documentType":"Assignment",
    "studentName":"Test Student",
    "studentId":"T001",
    "title":"Test",
    "instructor":"Prof. Test"
  }'

# Check file size to verify correct template used
ls -lh pattern-formatter/backend/outputs/
```

## Critical Points

| Item | ✅ CORRECT | ❌ WRONG |
|------|-----------|---------|
| Folder name | `Cover Pages _ Name` | `Cover_Pages_Name` |
| Spaces | Include spaces around `_` | No spaces around `_` |
| Template files | All 4 files present | Missing any file |
| ID format | lowercase: `uba`, `npui` | Mixed case: `UBA`, `Uba` |
| Fallback | Default: `'uba': ...` | Changes fallback (breaks backward compat) |

## Filenames (Must Match Exactly)

- `Assignments Cover Page Template.docx` - for Assignment doc type
- `Dissertation Cover Page Template.docx` - for Thesis/Dissertation doc types
- `Internship Cover Page Template.docx` - for Internship Report doc type
- `Research Proposal Cover Page Template.docx` - for Research Proposal doc type

## File Size Reference (After Generation)

These vary ±5-10% due to placeholder replacement:
- **Bamenda Assignment:** ~68KB
- **Buea Thesis:** ~210KB
- **NPUI Research:** ~112KB
- **BUST Assignment:** ~93KB (ADDED)
- **Catholic University Assignment:** ~225KB (ADDED)

If your new institution generates same size as Bamenda, it's using wrong template!

## Files to Update When Adding Institutions

1. ✅ Create folder: `pattern-formatter/Cover Pages/[Name]/`
2. ✅ Add 4 template files to folder
3. ✅ `pattern-formatter/backend/coverpage_generator.py` - Add to `institution_mapping`
4. ✅ `pattern-formatter/backend/data/institutions.json` - Add institution entry
5. ✅ `INSTITUTION_TEMPLATES_GUIDE.md` - Update supported institutions list

## Verification Checklist

Before marking as complete:
- [ ] Folder exists with exact name on disk
- [ ] All 4 template files in folder
- [ ] Code mapping added with exact folder name
- [ ] institutions.json updated with all departments
- [ ] Backend restarts without errors
- [ ] Can generate all 4 document types
- [ ] Generated file sizes differ from Bamenda
- [ ] Documentation updated

## Common Errors

| Error | Fix |
|-------|-----|
| Wrong template used | Verify folder name in code matches disk EXACTLY |
| Template not found | Check all 4 template files exist in folder |
| Institution doesn't appear in UI | Verify institutions.json syntax and API returns data |
| Backend crashes on startup | Check JSON syntax in institutions.json |
| Generated files are too small | Template was not found, falling back to default |

## Key Files

```
pattern-formatter/
├── backend/
│   ├── coverpage_generator.py          ← Institution mapping here (line ~51)
│   ├── data/
│   │   └── institutions.json           ← Institution data here
│   └── pattern_formatter_backend.py
├── Cover Pages/                        ← Templates folders here
│   ├── Cover Pages _ University of Bamenda/
│   ├── Cover Page _ University of Buea/
│   ├── Cover Pages _ National University Institute (NPUI)/
│   ├── Cover Page _ BUST/              ← ADDED
│   ├── Cover Page _ Catholic University/  ← ADDED
│   └── Cover Pages _ [NEW INSTITUTION]/
├── INSTITUTION_TEMPLATES_GUIDE.md      ← Detailed guide
├── NEW_INSTITUTION_CHECKLIST.md        ← Full checklist
├── NEW_INSTITUTIONS_IMPLEMENTATION_COMPLETE.md  ← BUST & CUCB details
└── INSTITUTION_QUICK_REFERENCE.md      ← This file
```

---

**Need more details?** See `INSTITUTION_TEMPLATES_GUIDE.md`

**Full checklist?** See `NEW_INSTITUTION_CHECKLIST.md`

**Issue with existing institution?** Check `coverpage_generator.py` line 51-60 for correct mappings
