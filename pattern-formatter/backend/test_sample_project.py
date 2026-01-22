"""
Test script to verify the hierarchy and certification preservation fixes.
Tests against sample_project_to_test.docx
"""
import sys
import os

# Add the backend path
backend_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_path)

from pattern_formatter_backend import DocumentProcessor, WordGenerator, FormatPolicy

def test_sample_document():
    """Test the document processing with sample_project_to_test.docx"""
    
    sample_path = os.path.join(
        os.path.dirname(os.path.dirname(backend_path)),
        'Samples',
        'sample_project_to_test.docx'
    )
    
    # Alternative path
    if not os.path.exists(sample_path):
        sample_path = r'c:\Users\user\Desktop\Afrodocs_dev\Afrodocs\Samples\sample_project_to_test.docx'
    
    if not os.path.exists(sample_path):
        print(f"ERROR: Sample file not found: {sample_path}")
        return False
    
    print(f"Processing: {sample_path}")
    print("=" * 60)
    
    # Create processor
    policy = FormatPolicy(preserve_existing_numbering=True)
    processor = DocumentProcessor(policy=policy)
    
    # Process the document
    try:
        result, images, shapes = processor.process_docx(sample_path)
        print(f"Processing complete!")
        print(f"  Images extracted: {len(images)}")
        print(f"  Shapes extracted: {len(shapes)}")
        
        analyzed = result.get('analyzed', [])
        structured = result.get('structured', [])
        stats = result.get('stats', {})
        
        print(f"\nStats:")
        print(f"  Total lines: {stats.get('total_lines', 0)}")
        print(f"  Headings: {stats.get('headings', 0)}")
        print(f"  Paragraphs: {stats.get('paragraphs', 0)}")
        
        # Check for hierarchy preservation
        print(f"\n{'='*60}")
        print("Checking hierarchy preservation:")
        print("-" * 60)
        
        hierarchical_headings = []
        protected_content = []
        
        for item in analyzed:
            if not isinstance(item, dict):
                continue
            
            text = item.get('text', '') or item.get('content', '')
            item_type = item.get('type', '')
            
            # Check for hierarchical numbers
            import re
            hierarchy_match = re.match(r'^(\d+(?:\.\d+)+)\s+', text)
            if hierarchy_match:
                num = hierarchy_match.group(1)
                depth = num.count('.') + 1
                hierarchical_headings.append({
                    'number': num,
                    'depth': depth,
                    'text': text[:60] + '...' if len(text) > 60 else text,
                    'type': item_type
                })
            
            # Check for protected content
            if item_type == 'protected_content' or item.get('is_protected'):
                protected_content.append({
                    'text': text[:60] + '...' if len(text) > 60 else text,
                    'type': item_type
                })
        
        print(f"\nFound {len(hierarchical_headings)} hierarchical headings:")
        for h in hierarchical_headings[:20]:  # Show first 20
            print(f"  [{h['depth']} levels] {h['number']}: {h['text']}")
        
        if len(hierarchical_headings) > 20:
            print(f"  ... and {len(hierarchical_headings) - 20} more")
        
        print(f"\nFound {len(protected_content)} protected content items:")
        for p in protected_content[:10]:
            print(f"  [{p['type']}] {p['text']}")
        
        # Check for deep hierarchies (3+ levels)
        deep_hierarchies = [h for h in hierarchical_headings if h['depth'] >= 3]
        print(f"\nDeep hierarchies (3+ levels): {len(deep_hierarchies)}")
        for h in deep_hierarchies[:10]:
            print(f"  {h['number']}: {h['text']}")
        
        # Generate output document
        output_path = os.path.join(backend_path, 'test_hierarchy_output.docx')
        print(f"\n{'='*60}")
        print(f"Generating output document: {output_path}")
        
        generator = WordGenerator(policy=policy)
        generator.generate(
            structured_data=structured,
            output_path=output_path,
            images=images,
            shapes=shapes,
            certification_data=None,  # Don't replace certification
            include_toc=False,
            font_size=12,
            line_spacing=1.5
        )
        
        print(f"Output document generated successfully!")
        print(f"\nPlease open {output_path} and verify:")
        print("  1. Hierarchical numbering is preserved (1.1, 1.1.1, etc.)")
        print("  2. Research questions/objectives are not duplicated")
        print("  3. Certification/Declaration pages have original content")
        
        return True
        
    except Exception as e:
        import traceback
        print(f"ERROR: {e}")
        traceback.print_exc()
        return False


if __name__ == '__main__':
    print("=" * 60)
    print("Testing Hierarchy and Content Preservation Fixes")
    print("=" * 60)
    
    success = test_sample_document()
    
    print("\n" + "=" * 60)
    if success:
        print("TEST COMPLETED SUCCESSFULLY! ✓")
    else:
        print("TEST FAILED! ✗")
    print("=" * 60)
