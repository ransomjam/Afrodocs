"""Test number_heading function"""
from pattern_formatter_backend import HeadingNumberer
import logging
logging.disable(logging.CRITICAL)

hn = HeadingNumberer()
hn.current_chapter = 1

tests = [
    '1.3.1 Main Research Questions',
    '2.1.1.1 Digital migration',
    '3.1.1 Scope of the Study',
    '1.1 Background to the Study',
]

for t in tests:
    result = hn.number_heading(t)
    print(f"Input: '{t}'")
    print(f"  -> numbered: '{result['numbered']}'")
    print(f"  -> number: '{result['number']}'")
    print(f"  -> was_renumbered: {result['was_renumbered']}")
    print()
