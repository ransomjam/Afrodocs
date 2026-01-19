# Complete Formatting Options Documentation

## Overview
The document formatter now supports comprehensive formatting customization for consistent document styling across all content.

## Formatting Parameters

### 1. Font Size
- **Parameter**: `font_size`
- **Type**: Integer (points)
- **Range**: 8-28pt
- **Default**: 12pt
- **Description**: Sets the base font size for body text. All content (paragraphs, lists, etc.) will use this size.
- **Heading Behavior**: Headings scale relative to body size:
  - Heading 1: base + 2pt
  - Heading 2: base + 1pt  
  - Heading 3: base
  - Title (Level 0): base + 4pt

### 2. Line Spacing
- **Parameter**: `line_spacing`
- **Type**: Float (multiplier)
- **Range**: 1.0-3.0
- **Default**: 1.5
- **Description**: Controls vertical spacing between lines throughout the document.
- **Impact**: Applied to all paragraph styles (body, headings, lists, captions, etc.)

### 3. Margins
The formatter supports two margin configuration modes:

#### Option A: Uniform Margins (Recommended for simplicity)
- **Parameter**: `margin_cm`
- **Type**: Float (centimeters)
- **Range**: 0.5-5.0cm
- **Default**: 2.5cm
- **Description**: Applies the same margin to all four sides

**Example:**
```
margin_cm=2.5  # All sides: 2.5cm
```

#### Option B: Individual Margin Control (For precise layouts)
- **Parameters**: 
  - `margin_left`: Left margin (cm)
  - `margin_top`: Top margin (cm)
  - `margin_bottom`: Bottom margin (cm)
  - `margin_right`: Right margin (cm)
- **Type**: Float (centimeters each)
- **Range**: 0.5-5.0cm each
- **Default**: 2.5cm per side
- **Description**: Configure each side independently for custom page layouts

**Example:**
```
margin_left=1.0     # Left edge
margin_top=2.0      # Top edge
margin_bottom=3.0   # Bottom edge
margin_right=4.0    # Right edge
```

### 4. Table of Contents
- **Parameter**: `include_toc`
- **Type**: Boolean (true/false)
- **Default**: false
- **Description**: When enabled, generates an automatic table of contents with page numbers

## API Usage Examples

### Example 1: Minimal Configuration (Using Defaults)
```bash
curl -F "file=@document.docx" http://localhost:5000/upload
```
Result: Default formatting (12pt, 1.5 spacing, 2.5cm uniform margins)

### Example 2: Larger Font with Adjusted Spacing
```bash
curl -F "file=@document.docx" \
  -F "font_size=18" \
  -F "line_spacing=2.0" \
  -F "margin_cm=3.0" \
  http://localhost:5000/upload
```

### Example 3: Individual Margins with TOC
```bash
curl -F "file=@document.docx" \
  -F "font_size=14" \
  -F "line_spacing=1.5" \
  -F "margin_left=2.0" \
  -F "margin_top=2.5" \
  -F "margin_bottom=2.5" \
  -F "margin_right=1.5" \
  -F "include_toc=true" \
  http://localhost:5000/upload
```

### Example 4: Accessibility-Friendly (Large Print)
```bash
curl -F "file=@document.docx" \
  -F "font_size=16" \
  -F "line_spacing=2.5" \
  -F "margin_cm=2.0" \
  http://localhost:5000/upload
```

## Formatting Consistency

All formatting is applied consistently throughout the document:

✓ **Body Text**: Uses specified font size and line spacing
✓ **Headings**: Scale relative to body font size
✓ **Lists**: Inherit base formatting
✓ **Tables**: Font size scales appropriately
✓ **Captions**: Font size = base - 2pt (minimum 8pt)
✓ **Cover Page**: Scales with user font size selection
✓ **Certification Pages**: Scales with user font size selection
✓ **Margins**: Applied uniformly to all sections

## Frontend Integration

When uploading documents, include these parameters:

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);
formData.append('font_size', '14');
formData.append('line_spacing', '1.8');
formData.append('margin_left', '2.0');
formData.append('margin_top', '2.5');
formData.append('margin_bottom', '2.5');
formData.append('margin_right', '2.0');
formData.append('include_toc', 'true');

const response = await fetch('/upload', {
  method: 'POST',
  body: formData
});
```

## Validation Rules

| Parameter | Min | Max | Unit | Default |
|-----------|-----|-----|------|---------|
| font_size | 8 | 28 | pt | 12 |
| line_spacing | 1.0 | 3.0 | ratio | 1.5 |
| margin_* | 0.5 | 5.0 | cm | 2.5 |

Invalid values are automatically clamped to valid ranges.

## Common Formatting Profiles

### Academic Paper
- font_size: 12pt
- line_spacing: 2.0
- margin_cm: 2.54 (1 inch)
- include_toc: true

### Business Document
- font_size: 11pt
- line_spacing: 1.15
- margin_cm: 2.0
- include_toc: false

### Large Print Document
- font_size: 18pt
- line_spacing: 2.5
- margin_cm: 2.0
- include_toc: false

### Compact Document
- font_size: 10pt
- line_spacing: 1.0
- margin_cm: 1.5
- include_toc: false

## Testing

Run the included test suite to verify formatting:
```bash
python test_margins.py        # Test margin configuration
python test_detailed_format.py # Test font size consistency
python test_consistency.py     # Test all formatting combinations
```

All tests should pass with consistent formatting across all document elements.
