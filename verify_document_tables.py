#!/usr/bin/env python3
"""Verify tables in the generated Word document"""

import os
import sys
from docx import Document

# Check the generated document
doc_path = r'C:\Users\user\AppData\Local\Temp\test_networking_notes.docx'

if os.path.exists(doc_path):
    doc = Document(doc_path)
    
    print("=" * 60)
    print("Verifying Tables in Generated Document")
    print("=" * 60)
    
    table_count = 0
    
    # Count tables in document
    for i, table in enumerate(doc.tables):
        table_count += 1
        row_count = len(table.rows)
        col_count = len(table.columns)
        print(f"\nTable {table_count}:")
        print(f"  Rows: {row_count}, Columns: {col_count}")
        
        # Print first few rows
        for row_idx, row in enumerate(table.rows[:2]):
            cells = [cell.text[:20] for cell in row.cells]
            print(f"    Row {row_idx}: {cells}")
    
    print(f"\n{'=' * 60}")
    print(f"Total tables found: {table_count}")
    
    if table_count >= 3:
        print("✓ SUCCESS: All 3 tables are present in the generated document!")
    else:
        print(f"✗ WARNING: Expected 3 tables, found {table_count}")
else:
    print(f"Document not found: {doc_path}")
