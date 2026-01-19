# New Institution Onboarding Checklist

Use this checklist when adding a new institution to prevent template mapping errors.

## Pre-Setup Validation

- [ ] Institution folder exists on disk at: `pattern-formatter/Cover Pages/[Exact Folder Name]/`
- [ ] Verify exact folder name using: `ls "pattern-formatter/Cover Pages"`
- [ ] Copy exact folder name (including ALL spaces, underscores, punctuation)
- [ ] Institution provides official Word document with departments/faculties/schools list

## Template Files Setup

- [ ] All 4 template files exist in the institution folder:
  - [ ] `Assignments Cover Page Template.docx`
  - [ ] `Dissertation Cover Page Template.docx`
  - [ ] `Internship Cover Page Template.docx`
  - [ ] `Research Proposal Cover Page Template.docx`
- [ ] Each template file is valid and opens without errors
- [ ] Templates have institution-specific branding/headers

## Code Updates

### Backend: `coverpage_generator.py`

- [ ] Updated docstring with new institution name and ID (around line 32)
- [ ] Added entries to `institution_mapping` dictionary (around line 51):
  ```python
  'xyz': 'Cover Pages _ [Exact Folder Name]',
  '[LegacyName]': 'Cover Pages _ [Exact Folder Name]',  # For backward compat
  ```
- [ ] Verify folder name in mapping matches EXACTLY with folder on disk (copy-paste!)
- [ ] Check: All institutions in mapping have entries
- [ ] Check: Folder names have spaces around underscores (if applicable)

### Backend: `institutions.json`

- [ ] Added new institution entry with:
  - [ ] `id`: lowercase ID (e.g., `xyz`)
  - [ ] `name`: Full institution name
  - [ ] `short`: Short code (e.g., `XYZ`)
  - [ ] `faculties`: Array with at least 1 faculty/school
  - [ ] Each faculty has `name` and `departments` array
  - [ ] All departments listed from official document
- [ ] JSON syntax is valid (use JSON validator)
- [ ] Array structure matches existing institutions

### Frontend: `index.html` (if manual updates needed)

- [ ] Verify institution appears in dropdown (should auto-populate from API)
- [ ] Test institution selection
- [ ] Test faculty/school selection cascading
- [ ] Test department selection cascading

## Testing & Validation

### API Testing

- [ ] Backend server starts without errors:
  ```bash
  cd pattern-formatter/backend
  py pattern_formatter_backend.py
  ```

- [ ] API endpoint returns institution in list:
  ```bash
  curl http://localhost:5000/api/institutions
  ```

- [ ] Can generate cover page for all document types:
  - [ ] Assignment (requires `instructor` field)
  - [ ] Thesis (requires `supervisor` field)
  - [ ] Internship Report (requires `academicSupervisor` and `fieldSupervisor` fields)
  - [ ] Research Proposal (requires `supervisor` field)

### File Validation

- [ ] Generated files saved to: `pattern-formatter/backend/outputs/`
- [ ] Each generated file is valid DOCX (can be opened in Word)
- [ ] File sizes:
  - [ ] Assignment: Record file size in bytes
  - [ ] Thesis: Record file size in bytes
  - [ ] Internship: Record file size in bytes
  - [ ] Research Proposal: Record file size in bytes
  - [ ] Verify sizes differ noticeably from other institutions (indicates different templates used)

### Content Verification

- [ ] Open generated DOCX files and verify:
  - [ ] Correct institution branding/name appears
  - [ ] Placeholders replaced with provided data
  - [ ] Format and layout match institution style
  - [ ] No Bamenda/Buea/NPUI content appears (unless intended)

## Documentation Updates

- [ ] Updated `INSTITUTION_TEMPLATES_GUIDE.md`:
  - [ ] Added to "Supported Institutions" section
  - [ ] Updated "Current Status" date
  - [ ] Added file sizes to reference data
- [ ] Updated this checklist with lessons learned (if any)

## Post-Deployment Checklist

- [ ] Frontend UI tested in browser
- [ ] Multiple cover pages generated successfully
- [ ] Tested on both desktop and mobile UI (if applicable)
- [ ] Files can be downloaded and opened
- [ ] No errors in backend logs
- [ ] Database records created for documents (if applicable)

## Troubleshooting Notes

If templates aren't working correctly, verify in this order:

1. **Check folder name on disk vs code:**
   ```powershell
   ls "c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages"
   ```
   Compare output with institution_mapping in code.

2. **Check template files exist:**
   ```powershell
   ls "c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages\[Folder Name]"
   ```
   Verify all 4 template files are listed.

3. **Verify API receives correct institution ID:**
   Check request payload in browser developer tools.

4. **Check generated file size:**
   If size matches Bamenda template, wrong template was used.

5. **Review backend logs:**
   Look for ERROR messages about template paths.

## Common Mistakes to Avoid

❌ **WRONG:** Folder name in code: `'xyz': 'Cover Pages_[Name]'` (missing spaces around underscore)
✅ **CORRECT:** Folder name in code: `'xyz': 'Cover Pages _ [Name]'` (spaces included)

❌ **WRONG:** Template files missing (e.g., only has Assignment, missing Thesis)
✅ **CORRECT:** All 4 template files present in folder

❌ **WRONG:** Institution ID in code doesn't match what frontend sends
✅ **CORRECT:** ID in institutions.json matches code mapping key

❌ **WRONG:** Departments listed but spellings don't match official document
✅ **CORRECT:** Exact copy of departments from official Word document

---

**Last Updated:** January 15, 2026
**Created for:** Preventing template mapping errors seen during University of Buea and NPUI implementation
