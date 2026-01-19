import os

# Check if template files exist
TEMPLATES_BASE = r"c:\Users\user\Desktop\PATTERN\pattern-formatter\Cover Pages"

folders = {
    'uba': 'Cover Pages_University of Bamenda',
    'ub': 'Cover Page_University of Buea',
    'npui': 'Cover Pages_National University Institute (NPUI)'
}

print("=" * 80)
print("CHECKING TEMPLATE FOLDER STRUCTURE")
print("=" * 80)

for inst_id, folder_name in folders.items():
    folder_path = os.path.join(TEMPLATES_BASE, folder_name)
    print(f"\n{inst_id.upper()}: {folder_name}")
    print(f"Path: {folder_path}")
    print(f"Exists: {os.path.exists(folder_path)}")
    
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        print(f"Files ({len(files)}):")
        for f in sorted(files):
            print(f"  - {f}")
    else:
        print("  ✗ FOLDER NOT FOUND!")

print("\n" + "=" * 80)
