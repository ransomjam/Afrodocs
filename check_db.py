import sqlite3
import os

# Check multiple possible database locations
db_paths = [
    'instance/users.db',
    'instance/app.db',
    '../instance/users.db',
    '../instance/app.db'
]

for db_path in db_paths:
    if os.path.exists(db_path):
        print(f"Found database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
            tables = cursor.fetchall()
            print("Tables:", [t[0] for t in tables])

            if 'user' in [t[0] for t in tables]:
                cursor.execute('SELECT username, plan, docs_this_month, pages_this_month, pages_balance FROM user ORDER BY id DESC LIMIT 5')
                users = cursor.fetchall()
                print('Recent users:')
                for user in users:
                    print(f'  {user[0]}: plan={user[1]}, docs={user[2]}, pages={user[3]}, balance={user[4]}')
            conn.close()
        except Exception as e:
            print(f"Error reading database: {e}")
        break
else:
    print("No database found")