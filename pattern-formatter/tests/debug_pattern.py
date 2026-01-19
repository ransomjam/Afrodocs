import sys
sys.path.insert(0, r'..\backend')
from pattern_formatter_backend import PatternEngine
engine = PatternEngine()
cases = ['**Warning:** System maintenance', '***CRITICAL UPDATE***', 'KEY POINTS', '**Important Notice**']
for c in cases:
    print('INPUT:', c)
    print('ANALYSIS:', engine.analyze_line(c, 0))
    print('---')
