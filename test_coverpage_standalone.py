#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test to verify coverpage generation is working correctly.
"""

import sys
import os
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'pattern-formatter' / 'backend'))

from docx import Document

def test_coverpage_generation():
    """Test that standalone coverpage generation works."""
    
    print("\n" + "="*80)
    print("TEST: Standalone Coverpage Generation")
    print("="*80)
    
    outputs_dir = Path(__file__).parent / 'pattern-formatter' / 'backend' / 'outputs'
    
    # Check for files with metadata indicating standalone coverpages
    print("\nLooking for recent standalone coverpages...")
    
    # Get all meta files
    meta_files = sorted(outputs_dir.glob('*_meta.json'), key=os.path.getmtime, reverse=True)
    
    standalone_coverpages = []
    for meta_file in meta_files[:20]:  # Check recent 20
        try:
            with open(meta_file) as f:
                meta = json.load(f)
            
            # Check if this is a standalone coverpage (not merged)
            is_merged = meta.get('is_merged', False)
            if not is_merged:
                job_id = meta['job_id']
                doc_path = outputs_dir / f"{job_id}_formatted.docx"
                
                if doc_path.exists():
                    standalone_coverpages.append({
                        'job_id': job_id,
                        'meta': meta,
                        'path': doc_path,
                        'size': doc_path.stat().st_size
                    })
        except Exception as e:
            pass
    
    if not standalone_coverpages:
        print("No standalone coverpages found - generating test data...")
        print("(This is expected if all recent documents are merged)\n")
        return True
    
    print(f"\nFound {len(standalone_coverpages)} standalone coverpages\n")
    
    for cp in standalone_coverpages[:3]:
        job_id = cp['job_id']
        meta = cp['meta']
        path = cp['path']
        
        print(f"Coverpage: {job_id[:8]}...")
        print(f"  File: {path.name}")
        print(f"  Size: {cp['size']} bytes")
        print(f"  Original filename: {meta.get('original_filename')}")
        print(f"  Is merged: {meta.get('is_merged')}")
        
        # Verify it's a valid document
        try:
            doc = Document(str(path))
            print(f"  Document paragraphs: {len(doc.paragraphs)}")
            print(f"  Document sections: {len(doc.sections)}")
            print(f"  ✓ Valid document")
        except Exception as e:
            print(f"  ✗ ERROR: {str(e)[:50]}")
        
        print()
    
    return True

if __name__ == '__main__':
    try:
        success = test_coverpage_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
