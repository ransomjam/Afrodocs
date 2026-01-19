# Document Formatting Options - Visual Guide

## User Interface

### Formatting Options Modal
When a user uploads or pastes a document, this modal appears:

```
┌─────────────────────────────────────────────┐
│  Document Formatting                    × │
├─────────────────────────────────────────────┤
│                                             │
│ ☐ Include Table of Contents               │
│   ↳ Automatically generate TOC, List of   │
│     Figures & Tables                      │
│                                             │
│ Font Size (pt)                              │
│ [▼] 12 pt (Standard)                        │
│                                             │
│ Line Spacing                                │
│ [▼] 1.5 (Standard)                          │
│                                             │
│ Margins (cm)                                │
│ [2.5    ]                                   │
│ Standard is 2.54 cm (1 inch)               │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Cancel  │  Process Document              │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

## Available Options

### 1. Table of Contents
- **Unchecked (Default)**: No TOC, List of Figures, or List of Tables
- **Checked**: Automatically generates all three based on document structure
- **Use Case**: Long documents with sections, figures, and tables

### 2. Font Size Options
- 10 pt (Small) - For dense content
- 11 pt - Slightly smaller than standard
- 12 pt (Standard) - Default, optimal readability
- 13 pt - Slightly larger
- 14 pt (Large) - For easier reading

**Backend Support**: 8pt-28pt range available (interface limits to common sizes)

### 3. Line Spacing Options
- 1.0 (Single) - Tight spacing, saves paper
- 1.15 - Slightly more than single
- 1.5 (Standard) - Default, optimal balance
- 2.0 (Double) - Double spacing, often required in academia

**Backend Support**: 1.0-3.0 range available

### 4. Margins
- Input any value from 0.5cm to 5.0cm
- Default: 2.5cm (approximately 1 inch)
- Common values:
  - 0.5cm: Minimal margins, more content per page
  - 1.0cm: Narrow margins
  - 2.0cm: Comfortable margins
  - 2.5cm (1 inch): Standard academic
  - 3.0cm: Wide margins
  - 5.0cm: Maximum margins

## How It Works

### For Uploaded Files
```
User selects file
        ↓
File validation (type check)
        ↓
Formatting Modal appears
        ↓
User selects options
        ↓
Click "Process Document"
        ↓
Options sent to backend
        ↓
Document processed with custom formatting
        ↓
Download ready
```

### For Pasted Text
```
User pastes text
        ↓
Text validation
        ↓
Formatting Modal appears
        ↓
User selects options
        ↓
Click "Process Document"
        ↓
Options sent to backend (text as file)
        ↓
Document processed with custom formatting
        ↓
Download ready
```

## Backend Processing

The backend receives the formatting options and applies them:

```python
# Extract options from request
include_toc = True/False
font_size = 10-28
line_spacing = 1.0-3.0
margin_cm = 0.5-5.0

# Apply to document
- Set margins on all sections
- Create AcademicBody style with font size & line spacing
- Generate TOC if include_toc is True
- Process document normally
```

## Key Features

✓ **Minimal Interface** - Only 4 simple options
✓ **All Optional** - Users can use defaults
✓ **Smooth Workflow** - Modal doesn't interrupt flow
✓ **Flexible** - Supports wide range of preferences
✓ **Validated** - Backend ensures safe values
✓ **Immediate Preview** - Effects visible in downloaded document

## Default Behavior

When user clicks "Process Document" without changing any options:
- Font Size: 12pt (Standard)
- Line Spacing: 1.5 (Standard)
- Margins: 2.5cm (1 inch)
- TOC: Not included

## Example Scenarios

### Scenario 1: Dense Academic Paper
- Font Size: 10pt
- Line Spacing: 1.0
- Margins: 2.0cm
- TOC: Yes (for large document)

### Scenario 2: Easy Reading
- Font Size: 14pt
- Line Spacing: 2.0
- Margins: 3.0cm
- TOC: No (short document)

### Scenario 3: Minimum Pages
- Font Size: 10pt
- Line Spacing: 1.0
- Margins: 0.5cm
- TOC: No

### Scenario 4: Professional Document
- Font Size: 12pt
- Line Spacing: 1.5
- Margins: 2.54cm
- TOC: Yes (if applicable)

## Implementation Notes

- Frontend: React state management with modal component
- Backend: Parameter validation and style application
- No database changes required
- Backward compatible with existing documents
- All options saved to output document properties
