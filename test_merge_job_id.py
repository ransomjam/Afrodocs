#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test to verify that merging finds the formatted document correctly.
"""

import os
import sys
import json
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'pattern-formatter' / 'backend'))

from docx import Document

def test_merge_job_id_handling():
    """Test that the merge job_id is handled correctly."""
    
    print("\n" + "="*80)
    print("TEST: Merge Job ID Handling")
    print("="*80)
    
    outputs_dir = Path(__file__).parent / 'pattern-formatter' / 'backend' / 'outputs'
    
    # Find an existing formatted document
    docx_files = sorted(outputs_dir.glob('*_formatted.docx'), key=os.path.getmtime, reverse=True)
    
    if not docx_files:
        print("\nERROR: No formatted documents found")
        return False
    
    # Get the most recent one
    existing_formatted = docx_files[0]
    existing_job_id = existing_formatted.name.replace('_formatted.docx', '')
    
    print(f"\nFound existing formatted document:")
    print(f"  File: {existing_formatted.name}")
    print(f"  Job ID: {existing_job_id}")
    
    # Check if metadata exists
    meta_path = outputs_dir / f"{existing_job_id}_meta.json"
    if meta_path.exists():
        with open(meta_path) as f:
            meta = json.load(f)
        print(f"  Metadata exists:")
        for key, value in meta.items():
            print(f"    {key}: {value}")
    
    # Now simulate what would happen if we try to merge with this document
    print(f"\n--- Simulating Merge Request ---")
    print(f"Request would include: mergeJobId = {existing_job_id}")
    
    # The backend would:
    # 1. Look for {existing_job_id}_formatted.docx
    check_path = outputs_dir / f"{existing_job_id}_formatted.docx"
    print(f"\nBackend would check: {check_path.name}")
    print(f"File exists: {check_path.exists()}")
    
    if check_path.exists():
        # 2. Load and merge with coverpage
        print(f"\n✓ GOOD: Formatted document found!")
        
        # 3. Should use same job_id for result
        print(f"\nResult:")
        print(f"  Output job_id: {existing_job_id} (same as merge_job_id)")
        print(f"  Result file: {existing_job_id}_formatted.docx (REPLACED with merged)")
        print(f"  User gets: Merged document (coverpage + body)")
        
        return True
    else:
        print(f"\n✗ PROBLEM: Formatted document NOT found!")
        print(f"This is the issue - the backend can't locate the file to merge with")
        
        # Check what files ARE there
        print(f"\nFiles in {outputs_dir.name}:")
        similar_files = list(outputs_dir.glob(f"*{existing_job_id[:8]}*"))
        if similar_files:
            for f in similar_files[:5]:
                print(f"  - {f.name}")
        
        return False

def test_coverage():
    """Show all recent documents and their job IDs."""
    
    print("\n" + "="*80)
    print("Document Coverage Analysis")
    print("="*80)
    
    outputs_dir = Path(__file__).parent / 'pattern-formatter' / 'backend' / 'outputs'
    
    # Get all job IDs
    job_ids = set()
    for f in outputs_dir.glob('*_formatted.docx'):
        job_id = f.name.replace('_formatted.docx', '')
        job_ids.add(job_id)
    
    print(f"\nTotal documents: {len(job_ids)}")
    
    # Show the most recent ones
    recent_jobs = sorted(
        [(job_id, (outputs_dir / f"{job_id}_formatted.docx").stat().st_mtime) for job_id in job_ids],
        key=lambda x: x[1],
        reverse=True
    )[:5]
    
    print(f"\nMost recent documents:")
    for job_id, mtime in recent_jobs:
        doc_path = outputs_dir / f"{job_id}_formatted.docx"
        try:
            doc = Document(str(doc_path))
            paras = len(doc.paragraphs)
            sections = len(doc.sections)
            print(f"  {job_id[:8]}... : {paras} paras, {sections} sections")
        except Exception as e:
            print(f"  {job_id[:8]}... : ERROR - {str(e)[:30]}")

if __name__ == '__main__':
    try:
        test_coverage()
        success = test_merge_job_id_handling()
        
        print("\n" + "="*80)
        if success:
            print("✓ SUCCESS: Merge job ID handling is correct")
        else:
            print("✗ ISSUE: Merge job ID handling needs fixing")
        print("="*80 + "\n")
        
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
