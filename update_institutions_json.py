#!/usr/bin/env python3
"""
Add new institutions to institutions.json
"""

import json

# Read the extracted data
with open('new_institutions_data.json', 'r', encoding='utf-8') as f:
    new_data = json.load(f)

# Read the current institutions.json
institutions_file = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\backend\data\institutions.json"
with open(institutions_file, 'r', encoding='utf-8') as f:
    current = json.load(f)

# Add new institutions
current['institutions'].append(new_data['bust'])
current['institutions'].append(new_data['catholic'])

# Save updated file
with open(institutions_file, 'w', encoding='utf-8') as f:
    json.dump(current, f, ensure_ascii=False, indent=2)

print(f"✅ Updated institutions.json with {len(current['institutions'])} institutions")
print("\nInstitutions in system:")
for inst in current['institutions']:
    total_depts = sum(len(f['departments']) for f in inst['faculties'])
    print(f"  - {inst['id']:10s} | {inst['name']:50s} | {total_depts:3d} departments")
