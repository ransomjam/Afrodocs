# Institution Template System - Visual Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Pattern Document Formatter                       │
│                   Institution Management System                     │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────┐         ┌──────────────────────────┐
│    FRONTEND (React)      │         │   BACKEND (Flask/Python) │
│                          │         │                          │
│  Institution Dropdown    │◄───────►│  /api/institutions       │
│  ├─ UBA                  │         │  └─ Returns JSON list    │
│  ├─ UB                   │         │                          │
│  └─ NPUI                 │         │  /api/coverpage/generate │
│                          │         │  └─ Loads correct template
│  Faculty/School Drop     │◄───────►│                          │
│  Department Drop         │         │  institutions.json       │
│                          │         │  └─ Data source          │
│  Generate button         │────────►│                          │
│  └─ Sends data + ID      │         │  coverpage_generator.py  │
│                          │         │  └─ template mapping     │
└──────────────────────────┘         └──────────────────────────┘
         │                                      │
         │                                      ▼
         │                           ┌──────────────────────────┐
         │                           │   Cover Pages Folder     │
         │                           │                          │
         │                           │ ├─ Bamenda/              │
         │                           │ │  ├─ Assignment.*       │
         │                           │ │  ├─ Thesis.*           │
         │                           │ │  ├─ Internship.*       │
         │                           │ │  └─ Research.*         │
         │                           │ │                        │
         │                           │ ├─ Buea/                 │
         │                           │ │  ├─ Assignment.*       │
         │                           │ │  ├─ Thesis.*           │
         │                           │ │  ├─ Internship.*       │
         │                           │ │  └─ Research.*         │
         │                           │ │                        │
         │                           │ └─ NPUI/                 │
         │                           │    ├─ Assignment.*       │
         │                           │    ├─ Thesis.*           │
         │                           │    ├─ Internship.*       │
         │                           │    └─ Research.*         │
         │                           └──────────────────────────┘
         │                                      │
         └─────────────────────────────────────►│
                   Generated DOCX                │
                   ├─ Correct branding          │
                   └─ Correct format             │
```

## Data Flow Diagram

```
┌─────────────────────────────────┐
│  User Selects Institution       │
│  Frontend: institution = "ub"   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  API Receives Request           │
│  POST /api/coverpage/generate   │
│  {institution: "ub", ...}       │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Backend: generate_cover_page()│
│  1. Extract institution ID      │
│  2. Call get_template_path()   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐         ┌──────────────────────┐
│  get_template_path()            │────────►│ institution_mapping  │
│  1. Get document type           │         │ {                    │
│  2. Map institution to folder   │         │  'ub': 'Cover Page _ │
│  3. Build path                  │         │   University of Buea'│
└──────────────┬──────────────────┘         └──────────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Template Path Built            │
│ /Cover Pages/                   │
│  Cover Page _ University of Buea│
│  /Dissertation Cover Page...    │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Load Template File             │
│  Document(template_path)        │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Replace Placeholders           │
│  {{studentName}} → "John Doe"   │
│  {{institution}} → "UB"         │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Save Generated Document        │
│  /backend/outputs/[job_id]...  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Return to Frontend             │
│  {success: true, filename: ...} │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  User Downloads Document        │
│  Correct branding + template    │
└─────────────────────────────────┘
```

## Institution Configuration Structure

```
institutions.json
{
  "institutions": [
    {
      "id": "uba",                          ◄─── Institution ID (used in code)
      "name": "The University of Bamenda",  ◄─── Display name
      "short": "UBa",                       ◄─── Abbreviation
      "logo": "uba_logo.png",               ◄─── Logo file
      "faculties": [                        ◄─── Array of faculties/schools
        {
          "name": "College of Technology",  ◄─── Faculty name
          "departments": [                  ◄─── Array of departments
            "Computer Engineering",
            "Telecommunications",
            ...more departments...
          ]
        },
        {
          "name": "School of Business",
          "departments": [...more depts...]
        }
      ]
    },
    { ...ub institution... },
    { ...npui institution... }
  ]
}
```

## Institution Mapping (In Code)

```python
# coverpage_generator.py - get_template_path() function

institution_mapping = {
    # University of Bamenda
    'uba': 'Cover Pages _ University of Bamenda',
    'Bamenda': 'Cover Pages _ University of Bamenda',    # Legacy support
    
    # University of Buea
    'ub': 'Cover Page _ University of Buea',             # Note: singular "Page"
    'Buea': 'Cover Page _ University of Buea',           # Legacy support
    
    # National University Institute
    'npui': 'Cover Pages _ National University Institute (NPUI)',
    'NPUI': 'Cover Pages _ National University Institute (NPUI)',  # Legacy
}

# CRITICAL: Folder names MUST match exactly with folders on disk
# DO NOT change these without verifying the folder exists first
```

## Document Types & Templates

```
┌──────────────────┬──────────────────────────┬──────────────────────┐
│ Document Type    │ Template Filename        │ Used For             │
├──────────────────┼──────────────────────────┼──────────────────────┤
│ Assignment       │ Assignments Cover Page   │ Course assignments   │
│                  │ Template.docx            │                      │
├──────────────────┼──────────────────────────┼──────────────────────┤
│ Thesis           │ Dissertation Cover Page  │ Thesis/dissertations │
│ Dissertation     │ Template.docx            │                      │
├──────────────────┼──────────────────────────┼──────────────────────┤
│ Internship       │ Internship Cover Page    │ Internship reports   │
│ Report           │ Template.docx            │                      │
├──────────────────┼──────────────────────────┼──────────────────────┤
│ Research         │ Research Proposal Cover  │ Research proposals   │
│ Proposal         │ Page Template.docx       │                      │
└──────────────────┴──────────────────────────┴──────────────────────┘
```

## Recent Fix - Before & After

```
BEFORE (JAN 15, 2026 - BUG):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Institution "ub" requested → Code: 'Cover Page_University of Buea'
Disk has: 'Cover Page _ University of Buea' (with spaces)
Result: File not found! Falls back to default: Bamenda
Generated: WRONG - Shows Bamenda templates instead of Buea

AFTER (JAN 15, 2026 - FIXED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Institution "ub" requested → Code: 'Cover Page _ University of Buea'
Disk has: 'Cover Page _ University of Buea' (MATCHES!)
Result: File found! Loads correct template
Generated: ✓ CORRECT - Shows Buea templates
```

## File Size Verification Method

```
To verify correct template is used, check generated file sizes:

Bamenda institution:
├─ Assignment: ~68 KB
├─ Thesis: ~75 KB
├─ Internship: ~79 KB
└─ Research: ~80 KB

Buea institution:
├─ Assignment: ~214 KB    ◄─ Significantly larger = different template!
├─ Thesis: ~210 KB
├─ Internship: ~215 KB
└─ Research: ~216 KB

NPUI institution:
├─ Assignment: ~109 KB    ◄─ Medium size = different template!
├─ Thesis: ~109 KB
├─ Internship: ~114 KB
└─ Research: ~112 KB

If new institution shows ~68-80 KB, wrong template is being used!
```

## Adding a New Institution - Visual Process

```
STEP 1: Create Folder
┌────────────────────────────────────────────┐
│ pattern-formatter/Cover Pages/             │
│ ├─ Existing institutions...                │
│ └─ NEW: Cover Pages _ [Institution Name]/  │
│        ├─ Assignments Cover...docx         │
│        ├─ Dissertation Cover...docx        │
│        ├─ Internship Cover...docx          │
│        └─ Research Proposal Cover...docx   │
└────────────────────────────────────────────┘

STEP 2: Update Code
┌────────────────────────────────────────────┐
│ backend/coverpage_generator.py (line ~51)  │
│                                            │
│ 'new_id': 'Cover Pages _ New Institution'  │
│                                            │
│ (COPY folder name exactly from disk!)      │
└────────────────────────────────────────────┘

STEP 3: Update Data
┌────────────────────────────────────────────┐
│ backend/data/institutions.json             │
│                                            │
│ Add new entry:                             │
│ {                                          │
│   "id": "new_id",                          │
│   "name": "Full Institution Name",         │
│   "faculties": [{...}, {...}]              │
│ }                                          │
└────────────────────────────────────────────┘

STEP 4: Test & Verify
┌────────────────────────────────────────────┐
│ 1. Restart backend                         │
│ 2. Generate all 4 document types           │
│ 3. Check file sizes differ from Bamenda    │
│ 4. Verify branding is correct              │
│ 5. Update documentation                    │
└────────────────────────────────────────────┘
```

## Documentation Map

```
README_INSTITUTIONS.md (You are here)
│
├─► NEW_INSTITUTION_CHECKLIST.md
│   └─ Use when adding new institutions
│
├─► INSTITUTION_QUICK_REFERENCE.md
│   └─ Use for quick facts and common issues
│
├─► INSTITUTION_TEMPLATES_GUIDE.md
│   └─ Use for detailed information and troubleshooting
│
├─► INSTITUTION_IMPLEMENTATION_SUMMARY.md
│   └─ Use for context and history
│
└─► This file (System Architecture)
    └─ Visual overview and diagrams
```

---

**Version:** v1.0  
**Last Updated:** January 15, 2026  
**Purpose:** Visual reference for institution template system architecture
