from pattern_formatter_backend import PatternEngine
pe = PatternEngine()
tests = [
    'themes—history',
    'wisdom—with',
    '1940–1950',
    'range 1940–1950 is shown',
    'word--word',
    'A long dash — between clauses',
    'En–dash used',
]
for t in tests:
    cleaned,_ = pe.clean_ai_content(t)
    print(f"{t!r} -> {cleaned!r}")
