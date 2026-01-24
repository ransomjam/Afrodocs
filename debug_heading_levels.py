"""Debug script to check heading levels and page break logic"""
import re

# Simulating the logic from pattern_formatter_backend.py

test_headings = [
    ('ACKNOWLEDGEMENT', 1),
    ('5.1 Recommendations', 2),
    ('5.1.1 Recommendations to Management', 3),
    ('5.1.2 Recommendations to University Administrators', 3),
    ('5.2 Conclusion', 2),
    ('CHAPTER FIVE', 1),
    ('CONCLUSION', 1),
    ('2.0 Background', 2),
    ('2.1 Literature Review', 2),
]

force_break_headings = [
    'RESUME', 'RÉSUMÉ', 'RÉSUME', 'RESUMÉ', 
    'ACKNOWLEDGEMENTS', 'ACKNOWLEDGMENTS', 'ACKNOWLEDGEMENT', 'ACKNOWLEDGMENT',
    'INTRODUCTION',
    'LITERATURE REVIEW',
    'METHODOLOGY', 'RESEARCH METHODOLOGY',
    'RESULTS', 'FINDINGS', 'DATA ANALYSIS',
    'DISCUSSION', 'FINDINGS AND DISCUSSION',
    'CONCLUSION', 'SUMMARY', 'RECOMMENDATIONS'
]

print("Testing heading analysis:")
print("=" * 80)

for heading, section_level in test_headings:
    heading_text = heading.strip().upper()
    
    # Check for numbered sub-section
    is_numbered_subsection = bool(re.match(r'^\d+\.\d+', heading_text))
    
    # Check for keyword match
    keyword_match = any(h in heading_text for h in force_break_headings)
    if keyword_match:
        matched_keywords = [h for h in force_break_headings if h in heading_text]
    else:
        matched_keywords = []
    
    # Evaluate if page break would be applied
    would_get_page_break = (
        section_level == 1 and 
        not is_numbered_subsection and 
        keyword_match
    )
    
    print(f"\nHeading: '{heading}'")
    print(f"  Section Level: {section_level}")
    print(f"  Heading Text (upper): '{heading_text}'")
    print(f"  Is Numbered Subsection: {is_numbered_subsection}")
    print(f"  Keyword Match: {keyword_match}")
    if matched_keywords:
        print(f"  Matched Keywords: {matched_keywords}")
    print(f"  >>> Would Get Page Break: {would_get_page_break}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
