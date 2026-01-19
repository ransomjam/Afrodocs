import sys
sys.path.append('../backend')
from pattern_formatter_backend import PatternEngine

# Test the new conservative table patterns
engine = PatternEngine()

# Test markdown table
test_markdown = '| Header 1 | Header 2 | Header 3 |'

print('Testing markdown table:')
result = engine.analyze_line(test_markdown, 1)
print('Type:', result['type'], 'Subtype:', result.get('subtype'))

# Test tab-separated table
test_tab = 'Name\tAge\tCity'

print('Testing tab-separated table:')
result = engine.analyze_line(test_tab, 2)
print('Type:', result['type'], 'Subtype:', result.get('subtype'))

print('Test completed successfully!')