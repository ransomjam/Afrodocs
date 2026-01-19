# Institution Management - Complete Documentation Index

This directory contains comprehensive documentation for managing institutions and cover page templates in the Pattern Document Formatter system.

## Quick Navigation

### 🚀 **START HERE** - Choose Your Scenario

**I'm adding a new institution:**
→ Read `INSTITUTION_QUICK_REFERENCE.md` first (5 min)  
→ Then follow `NEW_INSTITUTION_CHECKLIST.md` (step-by-step)  
→ Reference `INSTITUTION_TEMPLATES_GUIDE.md` as needed (details)

**I'm debugging a template issue:**
→ Go to `INSTITUTION_TEMPLATES_GUIDE.md` → Troubleshooting section

**I want to understand the system:**
→ Start with `INSTITUTION_IMPLEMENTATION_SUMMARY.md` (overview)  
→ Then read `INSTITUTION_TEMPLATES_GUIDE.md` (full details)

**I need a quick reminder:**
→ Use `INSTITUTION_QUICK_REFERENCE.md` (always available)

---

## Documents Overview

### 1. 📋 **NEW_INSTITUTION_CHECKLIST.md**
**What:** Complete step-by-step checklist  
**When to use:** When actually implementing a new institution  
**Read time:** 10 minutes  
**Sections:**
- Pre-setup validation
- Template files setup
- Code updates (both files)
- Testing & validation
- Post-deployment checklist
- Troubleshooting

### 2. 📖 **INSTITUTION_TEMPLATES_GUIDE.md**
**What:** Comprehensive developer guide with full context  
**When to use:** When you need detailed explanations and background  
**Read time:** 20 minutes  
**Sections:**
- Overview and current status
- Recent fix explanation (what went wrong, why, how fixed)
- Step-by-step institution addition guide
- Naming conventions (critical!)
- Code references
- Prevention strategies
- Version history

### 3. ⚡ **INSTITUTION_QUICK_REFERENCE.md**
**What:** TL;DR quick start guide  
**When to use:** When you just need the essentials quickly  
**Read time:** 5 minutes  
**Sections:**
- 5-minute setup overview
- Critical points comparison table
- File size reference data
- Common errors and fixes
- Key files locations

### 4. 📊 **INSTITUTION_IMPLEMENTATION_SUMMARY.md**
**What:** Executive summary and context  
**When to use:** When understanding what was done and why  
**Read time:** 10 minutes  
**Sections:**
- What was fixed and why
- Prevention strategy
- Documentation created
- Current system status
- Future implementation workflow
- Error prevention measures

---

## Key Facts to Remember

### Institutions Currently Supported
```
Institution ID    | Folder Name (EXACT - copy this)
─────────────────┼──────────────────────────────────────────
uba              | Cover Pages _ University of Bamenda
ub               | Cover Page _ University of Buea (Note: singular "Page")
npui             | Cover Pages _ National University Institute (NPUI)
```

### Critical Folder Naming Rule
When adding a new institution, the folder name MUST be copied EXACTLY from disk.
```
✅ CORRECT:   'Cover Pages _ University of Name'  (with spaces around underscore)
❌ WRONG:     'Cover_Pages_University_of_Name'    (underscores without spaces)
```

### Files to Update (Every Institution)
1. Create folder: `pattern-formatter/Cover Pages/[Exact Name]/`
2. Add 4 template files to folder
3. Update `backend/coverpage_generator.py` (add to mapping)
4. Update `backend/data/institutions.json` (add institution data)

### Testing Verification
After implementation, generated files should:
- Have different file sizes for different institutions (proves correct template used)
- Contain correct institution branding/name
- Be valid DOCX files that open in Microsoft Word

---

## The Problem That Was Fixed

**Issue:** All institutions were using Bamenda templates  
**Root Cause:** Folder names in code didn't match folder names on disk (spaces missing)  
**Fixed:** Updated folder name mapping with exact names from disk  
**Result:** Each institution now uses its own templates correctly  

See `INSTITUTION_IMPLEMENTATION_SUMMARY.md` for full context.

---

## How to Add a New Institution - Quick Overview

```
1. CREATE FOLDER
   └─ pattern-formatter/Cover Pages/Cover Pages _ [Institution Name]/
      ├─ Assignments Cover Page Template.docx
      ├─ Dissertation Cover Page Template.docx
      ├─ Internship Cover Page Template.docx
      └─ Research Proposal Cover Page Template.docx

2. UPDATE CODE
   └─ backend/coverpage_generator.py (around line 51)
      Add: 'xyz': 'Cover Pages _ [Institution Name]'

3. UPDATE DATA
   └─ backend/data/institutions.json
      Add institution entry with faculties and departments

4. TEST
   └─ Restart backend
   └─ Generate cover pages for all 4 document types
   └─ Verify file sizes differ from Bamenda
```

**Full detailed steps:** See `NEW_INSTITUTION_CHECKLIST.md`

---

## Troubleshooting Quick Links

| Problem | Solution |
|---------|----------|
| Wrong template being used | Check folder name in code matches disk EXACTLY (spaces!) |
| Template file not found | Verify all 4 template files exist in folder |
| Institution doesn't appear | Check institutions.json JSON syntax |
| Backend won't start | Check institutions.json for JSON errors |
| Generated file too small | Template file wasn't found, reverted to Bamenda |

For more troubleshooting, see `INSTITUTION_TEMPLATES_GUIDE.md` → Troubleshooting section.

---

## Code References

### Key Files for Institution Management

```
pattern-formatter/
├── backend/
│   ├── coverpage_generator.py
│   │   └─ Function: get_template_path() [Line 32-65]
│   │   └─ Institution mapping [Line 51-60]
│   │
│   ├── data/
│   │   └─ institutions.json [Contains all institution definitions]
│   │
│   └── pattern_formatter_backend.py
│       └─ Route: /api/coverpage/generate (POST)
│       └─ Route: /api/institutions (GET)
│
├── frontend/
│   └─ index.html
│       └─ Institution dropdown (populated from API)
│
└── Cover Pages/
    ├─ Cover Pages _ University of Bamenda/
    ├─ Cover Page _ University of Buea/
    ├─ Cover Pages _ National University Institute (NPUI)/
    └─ [Reserved for future institutions]
```

---

## Version & History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | Jan 15, 2026 | Fixed institution template mapping, created comprehensive documentation |

---

## FAQ

**Q: Can I use different folder naming conventions?**  
A: No. The folder name on disk MUST match the code mapping exactly. Use the format shown above.

**Q: What if I forget to add all 4 template files?**  
A: Users will get "template not found" errors when trying to generate those document types.

**Q: Can I change the default institution?**  
A: Yes, but only in line 61 of `coverpage_generator.py`. Bamenda is current default for backward compatibility.

**Q: What if two institutions use the same templates?**  
A: Create separate folders and separate mappings anyway. This ensures future changes don't affect both institutions.

**Q: How do I test my new institution?**  
A: Generate a cover page for each document type and verify: (1) correct branding appears, (2) file size differs from Bamenda.

---

## Support & Questions

- **General questions:** See `INSTITUTION_TEMPLATES_GUIDE.md`
- **Step-by-step help:** See `NEW_INSTITUTION_CHECKLIST.md`
- **Quick reference:** See `INSTITUTION_QUICK_REFERENCE.md`
- **Context/history:** See `INSTITUTION_IMPLEMENTATION_SUMMARY.md`

---

**Created:** January 15, 2026  
**Purpose:** Document institution management to prevent future template mapping errors  
**Audience:** Backend developers, QA testers, DevOps engineers
