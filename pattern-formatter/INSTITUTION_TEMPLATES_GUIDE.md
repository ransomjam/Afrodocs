# Institution Template Mapping - Developer Guide

## Overview
This document provides guidelines for managing cover page templates for different institutions in the Pattern Document Formatter system.

## Current Status (January 15, 2026)

### Supported Institutions
1. **University of Bamenda (UBA)**
   - Folder: `Cover Pages _ University of Bamenda/`
   - Institution ID: `uba`
   - Templates: Assignment, Thesis, Internship, Research Proposal

2. **University of Buea (UB)**
   - Folder: `Cover Page _ University of Buea/`
   - Institution ID: `ub`
   - Templates: Assignment, Thesis, Internship, Research Proposal

3. **National University Institute (NPUI)**
   - Folder: `Cover Pages _ National University Institute (NPUI)/`
   - Institution ID: `npui`
   - Templates: Assignment, Thesis, Internship, Research Proposal

## Recent Fix (January 15, 2026)

### Issue
All institutions were using Bamenda templates instead of their own institution-specific templates. Cover pages generated for Buea and NPUI were incorrectly showing Bamenda branding and format.

### Root Cause
The template folder names in the backend code had incorrect formatting:
- **Incorrect format:** `Cover Pages_University of Bamenda` (underscores without spaces)
- **Correct format:** `Cover Pages _ University of Bamenda` (underscores WITH spaces)

The actual folder names on disk have spaces around the underscore, but the code mapping was missing these spaces, causing file path lookup failures that silently fell back to Bamenda as the default.

### Solution Applied
Updated `pattern-formatter/backend/coverpage_generator.py` lines 51-60 with correct folder name mapping:

```python
institution_mapping = {
    'uba': 'Cover Pages _ University of Bamenda',
    'Bamenda': 'Cover Pages _ University of Bamenda',
    'ub': 'Cover Page _ University of Buea',
    'Buea': 'Cover Page _ University of Buea',
    'npui': 'Cover Pages _ National University Institute (NPUI)',
    'NPUI': 'Cover Pages _ National University Institute (NPUI)',
}
```

## Adding New Institutions

### Step 1: Create Folder Structure
Create a new folder under `pattern-formatter/Cover Pages/` with the naming convention:
```
Cover Pages _ [Institution Name]/
```
OR
```
Cover Page _ [Institution Name]/
```

### Step 2: Add Template Files
Inside the folder, add the following template files:
- `Assignments Cover Page Template.docx`
- `Dissertation Cover Page Template.docx`
- `Internship Cover Page Template.docx`
- `Research Proposal Cover Page Template.docx`

### Step 3: Update Backend Mapping
Edit `pattern-formatter/backend/coverpage_generator.py` in the `get_template_path()` function:

1. Add new entries to the `institution_mapping` dictionary (around line 51):
```python
institution_mapping = {
    'uba': 'Cover Pages _ University of Bamenda',
    'ub': 'Cover Page _ University of Buea',
    'npui': 'Cover Pages _ National University Institute (NPUI)',
    # NEW INSTITUTION - Add here:
    'xyz': 'Cover Pages _ [Your Institution Name]',
    '[Name]': 'Cover Pages _ [Your Institution Name]',  # Legacy name support
}
```

2. Update the default fallback if this is the new default institution (line 61):
```python
university_folder = institution_mapping.get(university, 'Cover Pages _ University of Bamenda')
# Keep Bamenda as default for backward compatibility, OR change to your new institution
```

### Step 4: Update Frontend Data
Edit `pattern-formatter/backend/data/institutions.json` to add the new institution:

```json
{
  "id": "xyz",
  "name": "Your Institution Name",
  "short": "XYZ",
  "logo": "xyz_logo.png",
  "faculties": [
    {
      "name": "Faculty/School Name",
      "departments": [
        "Department 1",
        "Department 2"
      ]
    }
  ]
}
```

### Step 5: Test
1. Restart the backend server:
   ```bash
   cd pattern-formatter/backend
   py pattern_formatter_backend.py
   ```

2. Generate a cover page for your new institution via the API:
   ```python
   payload = {
       'institution': 'xyz',
       'faculty': 'Faculty Name',
       'department': 'Department Name',
       'documentType': 'Assignment',
       'studentName': 'Test Student',
       'studentId': 'TEST001',
       'title': 'Test Title',
       'instructor': 'Prof. Test'
   }
   response = requests.post('http://localhost:5000/api/coverpage/generate', json=payload)
   ```

3. Verify file size matches expected template size (allows for 5-10% variation due to placeholder replacement)

## Critical Naming Conventions

### ⚠️ IMPORTANT: Folder Naming Format
Folder names on disk MUST match exactly in the code mapping:
- Check the actual folder name on disk (use `ls` or File Explorer)
- Copy the exact name including ALL spaces and punctuation
- Example: `"Cover Pages _ University of Bamenda"` (note the spaces around underscore)

### Institution ID Conventions
- Use lowercase alphanumeric (e.g., `uba`, `ub`, `npui`)
- Add both lowercase and full name variants to support legacy parameters
- Example:
  ```python
  'uba': 'Cover Pages _ University of Bamenda',
  'Bamenda': 'Cover Pages _ University of Bamenda',  # Backward compatibility
  ```

### Folder Naming Pattern
Use one of these patterns (chosen to match actual folder names):
- `Cover Pages _ [Institution Name]/` (with spaces around underscore)
- `Cover Page _ [Institution Name]/` (singular "Page" if applicable)

## File Path Resolution
The template path is constructed as:
```python
os.path.join(TEMPLATES_DIR, university_folder, filename)
```
Which resolves to:
```
pattern-formatter/Cover Pages/[Institution Folder]/[Template Filename]
```

Example for Buea Thesis:
```
pattern-formatter/Cover Pages/Cover Page _ University of Buea/Dissertation Cover Page Template.docx
```

## Data Files
- **Institutions Data:** `pattern-formatter/backend/data/institutions.json`
  - Source of truth for institution list, faculties, and departments
  - Used by API endpoint `/api/institutions`
  - Served to frontend for dropdown population

- **Department Data:** Extract from official Word documents provided by each institution
  - `The University of Bamenda _ Schools-Faculties-Departments.docx`
  - `University of Buea _ Schools-Faculties-Departments.docx`
  - `National University Institute (NPUI) _ Schools-Faculties-Departments.docx`

## Code References

### Backend Files
- **Main Template Handler:** `pattern-formatter/backend/coverpage_generator.py`
  - Function: `get_template_path(document_type, university='uba')`
  - Function: `generate_cover_page(data)`

- **Backend API:** `pattern-formatter/backend/pattern_formatter_backend.py`
  - Route: `/api/coverpage/generate` (POST)
  - Route: `/download/<job_id>` (GET)
  - Route: `/download-pdf/<job_id>/<filename>` (GET)

### Frontend Files
- **Main UI:** `pattern-formatter/frontend/index.html`
  - Institution dropdown selector (populated from API)
  - Faculty/School selector (cascading)
  - Department selector (cascading)
  - Form submission to `/api/coverpage/generate`

## Prevention Strategy

### Validation on Addition
Before marking a new institution as complete:

1. ✅ Verify folder name exists on disk
2. ✅ Verify all template files exist in folder
3. ✅ Verify mapping in code matches folder name EXACTLY (including spaces)
4. ✅ Test API with all document types (Assignment, Thesis, Internship, Research Proposal)
5. ✅ Verify generated files differ by file size from other institutions
6. ✅ Update this documentation

### Testing Commands
```bash
# Check folder exists and contents
ls "pattern-formatter/Cover Pages"

# Generate test cover page
curl -X POST http://localhost:5000/api/coverpage/generate \
  -H "Content-Type: application/json" \
  -d '{"institution":"uba","faculty":"Test","department":"Test","documentType":"Assignment","studentName":"Test","studentId":"T001","title":"Test"}'

# Check generated file
ls -lh "pattern-formatter/backend/outputs/"
```

## Troubleshooting

### Issue: Wrong template used for new institution
**Cause:** Folder name in code doesn't match actual folder name on disk
**Fix:** 
1. Check exact folder name: `ls "pattern-formatter/Cover Pages"`
2. Copy exact name to code mapping (watch for spaces)
3. Restart backend

### Issue: Template file not found error
**Cause:** Folder exists but template filename is wrong
**Fix:**
1. Check template filenames in folder: `ls "pattern-formatter/Cover Pages/[Folder]/"`
2. Ensure all 4 template files exist
3. Use exact filenames: `Assignments Cover Page Template.docx`, `Dissertation Cover Page Template.docx`, etc.

### Issue: Generated file has wrong branding
**Cause:** `institution_mapping` fallback is being used
**Fix:**
1. Check institution ID being sent matches mapping key
2. Verify code change was saved and backend restarted
3. Check file size to identify which template was actually used

## Version History

### v1.0 (January 15, 2026)
- Fixed folder name mapping to use correct format with spaces
- Added support for University of Buea and NPUI institutions
- Created this documentation
- Current: 3 institutions supported (Bamenda, Buea, NPUI)

