"""
VISUAL WORKFLOW DIAGRAM: How the Fix Works
===========================================

BEFORE FIX (❌ Problem):
========================

User Document (Justified) ──format──> Formatted Doc ──add_coverpage──> Merged Doc (❌ Justification LOST!)
                                             ✓                               ✓ Merge successful
                                      (Justified)                       (Formatting lost - why?)

                                    
The Problem:
─────────────
1. User formats document → Body content is justified ✓
2. User adds coverpage → Merge happens with Composer
3. Formatter merges documents
4. But merge process resets paragraph formatting!
5. Result: Coverpage is there but body loses justification ❌


AFTER FIX (✅ Solution):
=========================

User Document (Justified) ──format──> Formatted Doc ──add_coverpage──> Merged Doc ──restore_format──> Final Doc
                                             ✓                               ✓              ✓          (✅ Justified!)
                                      (Justified)                    (Formatting lost)    (Formatting
                                                                                         RESTORED!)

                                    
The Solution:
──────────────
1. User formats document → Body content is justified ✓
2. User adds coverpage → Merge happens with Composer  
3. Formatter merges documents
4. Merge process resets paragraph formatting ✓ (normal behavior)
5. NEW: Formatter detects body paragraphs and restores formatting ✓
6. Result: Coverpage + justified body content ✓✓✓


TECHNICAL FLOW:
================

api_generate_coverpage(data):
    │
    ├─ Check if mergeJobId exists
    │  │
    │  └─ YES → Load cover_doc and processed_doc
    │     │
    │     ├─ Create AcademicBody styles (NEW: with Pt(12) instead of self.font_size)
    │     │
    │     ├─ Convert processed_doc paragraphs to Academic styles
    │     │  (Mark them for later identification)
    │     │
    │     ├─ Add NEW_PAGE section break
    │     │
    │     ├─ MERGE with Composer.append()
    │     │
    │     └─ SAVE merged_doc
    │
    └─ AFTER SAVE (NEW RESTORATION CODE):
       │
       ├─ Reload merged_doc
       │
       ├─ Iterate through sections > 1 (body sections only)
       │
       ├─ For each paragraph:
       │  ├─ IF style is AcademicBody/AcademicListNumber/AcademicListBullet:
       │  │  ├─ Set alignment = JUSTIFY ✓
       │  │  └─ Set line_spacing = 1.5 ✓
       │  │
       │  └─ ELSE IF substantial text (>10 chars) AND style is Normal/List*:
       │     ├─ Set alignment = JUSTIFY ✓
       │     └─ Set line_spacing = 1.5 ✓
       │
       ├─ For each table in merged_doc:
       │  └─ Apply same formatting to all cell paragraphs
       │
       └─ SAVE merged_doc (with formatting restored!)


KEY INSIGHT:
=============
The fix doesn't prevent formatting loss - it RESTORES it after the merge.
This is necessary because Composer.append() is a destructive operation
that resets many formatting properties. By explicitly restoring formatting
after merge, we preserve the user's original formatting intent.


FORMATTING PRESERVATION STRATEGY:
==================================

1. BEFORE MERGE: Mark body content
   ├─ Convert paragraphs to AcademicBody/AcademicListNumber/AcademicListBullet styles
   └─ This creates an "identity" for body content

2. DURING MERGE: Document composition
   ├─ Composer.append() merges documents
   └─ Formatting lost (expected/normal behavior)

3. AFTER MERGE: Restore formatting
   ├─ Identify body paragraphs by style name
   ├─ Find section > 1 (body section)
   ├─ Apply JUSTIFY alignment to all body paragraphs
   ├─ Apply 1.5 line spacing to all body paragraphs
   └─ Preserve coverpage (section 0) formatting as-is

4. SAVE RESULT: Document with preserved formatting
   └─ User gets coverpage + formatted body content ✓


RESULT COMPARISON:
===================

BEFORE FIX:
────────────
Formatted Document:
  Para 1: [AcademicBody] JUSTIFY ✓
  Para 2: [AcademicBody] JUSTIFY ✓
  Para 3: [AcademicBody] JUSTIFY ✓

After Coverpage Addition:
  Para 1: [Coverpage Title] LEFT ✓ (coverpage)
  Para 2: [Coverpage Form] LEFT ✓ (coverpage)
  Para 3: [AcademicBody] LEFT ❌ (LOST FORMATTING!)
  Para 4: [AcademicBody] LEFT ❌ (LOST FORMATTING!)
  Para 5: [AcademicBody] LEFT ❌ (LOST FORMATTING!)

AFTER FIX:
───────────
After Coverpage Addition (with restoration):
  Para 1: [Coverpage Title] LEFT ✓ (coverpage - unchanged)
  Para 2: [Coverpage Form] LEFT ✓ (coverpage - unchanged)
  Para 3: [AcademicBody] JUSTIFY ✓ (FORMATTING RESTORED!)
  Para 4: [AcademicBody] JUSTIFY ✓ (FORMATTING RESTORED!)
  Para 5: [AcademicBody] JUSTIFY ✓ (FORMATTING RESTORED!)

SUCCESS! ✓✓✓
"""