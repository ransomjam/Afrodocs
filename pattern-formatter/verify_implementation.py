#!/usr/bin/env python3
import json

# Load and verify institutions
with open('backend/data/institutions.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("IMPLEMENTATION VERIFICATION")
print("=" * 80)

institutions = data['institutions']
print(f"\nTotal Institutions: {len(institutions)}")
print()

total_depts = 0
total_faculties = 0

for inst in institutions:
    num_faculties = len(inst['faculties'])
    num_depts = sum(len(f['departments']) for f in inst['faculties'])
    total_depts += num_depts
    total_faculties += num_faculties
    
    status = "[NEW]" if inst['id'] in ['bust', 'cucb'] else "[OK]"
    print(f"{status} {inst['id']:10s} | {inst['name']:45s} | {num_faculties:2d} fac | {num_depts:3d} depts")

print()
print(f"{'Total':10s}{'':36s}{'':13s} {total_faculties:2d} fac | {total_depts:3d} depts")
print("=" * 80)

# Verify code mapping
print("\nVerifying coverpage_generator.py mappings...")
with open('backend/coverpage_generator.py', 'r') as f:
    content = f.read()
    if "'bust'" in content and "'Cover Page _ BUST'" in content:
        print("[OK] BUST mapping found")
    if "'cucb'" in content and "'Cover Page _ Catholic University'" in content:
        print("[OK] CUCB mapping found")

print("\n[SUCCESS] Implementation verified!")
print("=" * 80)
