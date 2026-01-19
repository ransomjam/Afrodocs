import requests
import time
import os

BASE_URL = 'http://localhost:5000'
USERNAME = f'limit_test_{int(time.time())}'
PASSWORD = 'password123'

def test_limit():
    session = requests.Session()
    
    # 1. Signup
    print(f"Registering user {USERNAME}...")
    res = session.post(f'{BASE_URL}/api/auth/signup', json={
        'username': USERNAME,
        'password': PASSWORD,
        'email': f'{USERNAME}@example.com'
    })
    if res.status_code not in [200, 201]:
        print(f"Signup failed: {res.text}")
        return
    print("Signup successful.")

    # 2. Login
    print("Logging in...")
    res = session.post(f'{BASE_URL}/api/auth/login', json={
        'username': USERNAME,
        'password': PASSWORD
    })
    if res.status_code != 200:
        print(f"Login failed: {res.text}")
        return
    print("Login successful.")

    # 3. Upload 4 times
    # Create a dummy file
    with open('test_doc.txt', 'w') as f:
        f.write('Test document content.')

    for i in range(1, 6):
        print(f"Upload attempt {i}...")
        with open('test_doc.txt', 'rb') as f:
            files = {'file': ('test_doc.txt', f, 'text/plain')}
            res = session.post(f'{BASE_URL}/upload', files=files)
        
        print(f"Status: {res.status_code}")
        if res.status_code == 200:
            print("Upload successful.")
        elif res.status_code == 403:
            print(f"Upload blocked as expected: {res.json()}")
            break
        else:
            print(f"Unexpected error: {res.text}")

    # Check status
    res = session.get(f'{BASE_URL}/api/auth/status')
    print(f"Final Status: {res.json()}")

if __name__ == '__main__':
    try:
        test_limit()
    except Exception as e:
        print(f"Test failed: {e}")
