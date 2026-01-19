import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
from pattern_formatter_backend import PatternEngine

p = PatternEngine()
print('PatternEngine OK')
print(p.analyze_line('REFERENCES', 0))
