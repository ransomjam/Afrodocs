# Document Formatting Options - Implementation Summary

## Overview
Added comprehensive document formatting options to the AfroDocs application. Users can now customize document appearance before processing, including table of contents, font size, line spacing, and margins.

## Features Added

### 1. Formatting Options Modal
A clean, minimal modal dialog appears when users upload or paste a document. The modal allows users to:
- **Include Table of Contents**: Toggle to include/exclude TOC, List of Figures, and List of Tables
- **Font Size**: Select from 10pt to 14pt (8pt-28pt supported in backend)
- **Line Spacing**: Choose between 1.0, 1.15, 1.5 (default), or 2.0
- **Margins**: Input custom margins in centimeters (0.5-5.0cm range, default 2.54cm/1 inch)

### 2. Frontend Changes (index.html)
**New State Variables:**
- `showFormattingModal`: Controls modal visibility
- `pendingFile`: Stores file before formatting options are applied
- `formattingOptions`: Object containing user-selected formatting values

**New Components:**
- `FormattingOptionsModal`: React component with form inputs for formatting options
  - Checkbox for TOC
  - Select dropdowns for font size and line spacing
  - Number input for margins

**Modified Handlers:**
- `handleFileSelect()`: Now shows modal instead of immediately processing
- `processFileWithOptions()`: New function that processes file with selected options
- `handlePasteSubmit()`: Updated to show modal before processing pasted text

**Modal Integration:**
The modal is rendered alongside other modals (PricingModal, PdfPreviewModal) at the end of the component.

### 3. Backend Changes (pattern_formatter_backend.py)

**Parameter Extraction in /upload endpoint:**
```python
include_toc = request.form.get('include_toc', 'false').lower() == 'true'
font_size = request.form.get('font_size', '12')
line_spacing = request.form.get('line_spacing', '1.5')
margin_cm = request.form.get('margin_cm', '2.5')
```

Parameters are validated and constrained to safe ranges:
- Font size: 8-28pt
- Line spacing: 1.0-3.0
- Margins: 0.5-5.0cm

**WordGenerator Class Updates:**
- Added formatting option instance variables in `__init__()`
- Updated `generate()` method signature to accept formatting parameters
- Applied custom margins to all document sections
- Applied font size and line spacing to the AcademicBody style
- Made TOC generation conditional based on `include_toc` parameter

**Style Application:**
The AcademicBody style is created with user-selected font size and line spacing, ensuring consistent formatting throughout the document.

## User Flow

1. **Upload/Paste Document**
   - User uploads file or pastes text
   - Formatting options modal appears

2. **Select Options** (All optional)
   - User can toggle TOC on/off
   - Select preferred font size
   - Choose line spacing
   - Adjust margins

3. **Process**
   - Click "Process Document" button
   - Options are sent to backend
   - Document is formatted according to preferences

4. **Download**
   - Download formatted DOCX or PDF
   - Formatting applied throughout the document

## Design Philosophy

The implementation follows these principles:
- **Minimal & Non-Intrusive**: Options don't affect app structure
- **Simple & Intuitive**: Users only see relevant options
- **Optional**: Users can use defaults if they don't need customization
- **Smooth**: Modal transitions are seamless
- **Accessible**: Clear labels and helpful hints

## Default Values

- Include TOC: Disabled (unchecked)
- Font Size: 12pt
- Line Spacing: 1.5
- Margins: 2.5cm (1 inch)

## Technical Details

### Frontend-Backend Communication
Formatting options are sent as form data alongside the file:
```
include_toc: "true" or "false"
font_size: "10" to "14"
line_spacing: "1.0" to "2.0"
margin_cm: "0.5" to "5.0"
```

### Document Generation Process
1. Margins applied to all sections immediately after Document() creation
2. AcademicBody style created with user-selected font size and line spacing
3. Cover page, certification page, and all content use these settings
4. TOC is only generated if `include_toc` is True

### Backward Compatibility
The parameters have default values, so existing code calling the generate() method without the new parameters will still work correctly.

## Testing Recommendations

1. **Test Various Combinations**:
   - With/without TOC
   - Different font sizes (10, 12, 14)
   - Different line spacings (1.0, 1.5, 2.0)
   - Different margins (0.5, 2.5, 5.0)

2. **Test With Different Document Types**:
   - Plain text (TXT)
   - Word documents (DOCX)
   - Markdown files (MD)

3. **Verify Output**:
   - Open generated DOCX files in Word/LibreOffice
   - Verify font sizes are applied
   - Check line spacing is correct
   - Confirm margins are as specified
   - Verify TOC appears when selected, absent when not

4. **Edge Cases**:
   - Very small margins (0.5cm)
   - Very large margins (5.0cm)
   - Large font sizes (14pt) with tight line spacing
   - Small font sizes (10pt) with wide line spacing

## Files Modified

1. `frontend/index.html` - Added modal and state management
2. `backend/pattern_formatter_backend.py` - Added parameter handling and formatting logic

## Notes

- The implementation is minimal and doesn't disrupt the existing document processing pipeline
- All formatting options are optional with sensible defaults
- The modal provides a smooth user experience
- The backend validates all parameters to ensure document integrity
