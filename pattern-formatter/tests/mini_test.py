import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
from pattern_formatter_backend import PatternEngine

p = PatternEngine()
cases = [
    'ABSTRACT',
    'CHAPTER 1: FOUNDATIONS',
    'REFERENCES',
    'KEY POINTS',
    'MAIN OBJECTIVES',
    '(a) Sub-point',
    'b) Lettered item with parenthesis',
    '1. Introduction',
]

for c in cases:
    res = p.analyze_line(c, 0)
    print(c, '->', res['type'], res.get('level', ''))
