import sys
sys.path.insert(0, '../backend')
from pattern_formatter_backend import PatternEngine

engine = PatternEngine()

# Test the specific spaced table detection
test_cases = [
    # Should be PARAGRAPHS (not tables)
    ('Cloud computing has fundamentally transformed enterprise IT', 'paragraph'),
    ('The global cloud market reached $912.77 billion in 2025', 'paragraph'),
    ('Organizations reduce IT expenditure by leveraging shared infrastructure', 'paragraph'),
    ('This transformation is significant for multiple reasons', 'paragraph'),

    # Should be TABLES
    ('ID     Name     Age', 'plain_table_row'),
    ('1      John     25', 'plain_table_row'),
    ('Component                      What It Does', 'plain_table_row'),
    ('Cloud servers                  Store and process videos', 'plain_table_row'),
]

print('Testing spaced table detection...')
for text, expected in test_cases:
    result = engine.analyze_line(text, 1)
    actual = result['type']
    status = 'PASS' if actual == expected else 'FAIL'
    print(f'{status}: {text[:50]}... -> {actual} (expected {expected})')