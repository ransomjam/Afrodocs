#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

try:
    from pattern_formatter_backend import PatternEngine
    p = PatternEngine()
    print('PatternEngine created successfully')
    print('Has _extract_cells method:', hasattr(p, '_extract_cells'))
    
    if hasattr(p, '_extract_cells'):
        result = p._extract_cells('Name    Age    City', 'spaced')
        print('Method result:', result)
        print('Test passed!')
    else:
        print('Method not found!')
        
except Exception as e:
    print('Error:', str(e))
    import traceback
    traceback.print_exc()