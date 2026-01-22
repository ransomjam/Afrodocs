import sqlite3
import os

# Find the database - try multiple possible locations
db_paths = [
    'instance/users.db',
    'instance/afrodocs.db',
    '../instance/users.db'
]

db_path = None
for path in db_paths:
    if os.path.exists(path):
        db_path = path
        break

if not db_path:
    print(f"Database not found in any location")
    exit(1)

print(f"Using database: {db_path}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(f"Tables: {tables}")

# Find the user table (might be named differently)
user_table = None
for table in tables:
    if 'user' in table[0].lower():
        user_table = table[0]
        break

if not user_table:
    print("No user table found!")
    exit(1)

print(f"Found user table: {user_table}")

# Check existing columns
cursor.execute(f"PRAGMA table_info({user_table})")
columns = cursor.fetchall()
existing_cols = [col[1] for col in columns]
print(f"Existing columns: {existing_cols}")

# Add missing columns
new_columns = [
    ('ai_requests_count', 'INTEGER DEFAULT 0'),
    ('created_at', 'DATETIME'),
    ('last_login', 'DATETIME'),
    ('last_activity', 'DATETIME')
]

for col_name, col_type in new_columns:
    if col_name not in existing_cols:
        try:
            cursor.execute(f"ALTER TABLE {user_table} ADD COLUMN {col_name} {col_type}")
            print(f"Added column: {col_name}")
        except Exception as e:
            print(f"Could not add {col_name}: {e}")
    else:
        print(f"Column {col_name} already exists")

conn.commit()
conn.close()
print("Migration complete!")
