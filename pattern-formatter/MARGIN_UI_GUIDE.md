# Frontend Margin Configuration Update

## What's New

The formatting options modal now includes a **toggle between two margin modes**:

### 1. Uniform Margins Mode (Default)
- Single input field for all four sides
- Quick and simple for standard documents
- Default value: 2.5 cm (1 inch)
- Click "Individual" button to switch mode

### 2. Individual Margins Mode
- Four separate input fields for each side
- Fine-grained control over page layout
- Specify each margin independently:
  - **Left** margin
  - **Top** margin
  - **Bottom** margin
  - **Right** margin
- Click "Uniform" button to switch back

## How to Use

### Step 1: Select Document
Upload a document (.docx, .txt, .md, .doc)

### Step 2: Click "Formatting Options"
The formatting modal will open

### Step 3: Configure Margins
- **For Uniform Margins**: Keep the "Individual" button and enter one value
- **For Individual Margins**: Click "Individual" button to expand four input fields

### Step 4: Set Other Options
- Font Size: 8-28 points
- Line Spacing: 1.0x - 3.0x
- Include TOC: Optional checkbox
- Other margins (if not using uniform)

### Step 5: Click "Process Document"
The document will be formatted with your selected margin configuration

## UI Features

- **Toggle Button**: Easy switching between uniform and individual margin modes
- **Grid Layout**: 2x2 grid for individual margin inputs when enabled
- **Responsive Design**: Margins adapt to screen size
- **Live Preview**: Form updates reflect changes immediately
- **Validation**: Input values are constrained to valid ranges (0.5-5.0 cm)

## Technical Implementation

### Frontend Changes
- Added `useIndividualMargins` state to track mode
- Added `marginLeft`, `marginTop`, `marginBottom`, `marginRight` to options state
- Updated form to conditionally show uniform or individual inputs
- Toggle button to switch between modes
- Form data submission sends appropriate parameters based on mode

### Backend Compatibility
- Fully backward compatible with uniform margin parameter
- Automatically detects which mode is being used
- Gracefully falls back to default values if parameters are missing

## Testing the Feature

1. Open the application at http://localhost:5000
2. Upload a test document
3. Click "Formatting Options"
4. Try both margin modes:
   - **Uniform Mode**: Set a single margin value (e.g., 2.5)
   - **Individual Mode**: Set different values for each side (e.g., L:1, T:2, B:3, R:4)
5. Process the document and verify margins in output

## Example Configurations

### Academic Paper
- Left: 2.54cm (1 inch)
- Top: 2.54cm
- Bottom: 2.54cm
- Right: 2.54cm

### Report with Wide Left Margin
- Left: 3.0cm (for binding)
- Top: 2.0cm
- Bottom: 2.0cm
- Right: 1.5cm

### Narrow Margins Document
- Left: 1.0cm
- Top: 1.0cm
- Bottom: 1.0cm
- Right: 1.0cm

### Asymmetric Layout
- Left: 2.0cm
- Top: 3.0cm
- Bottom: 2.5cm
- Right: 1.5cm
