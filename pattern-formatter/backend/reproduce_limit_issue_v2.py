import requests
import sys

BASE_URL = 'http://localhost:5000'

def register_and_login(username, password):
    # Register
    signup_payload = {
        'username': username,
        'password': password,
        'institution': 'Test Inst',
        'contact': '123',
        'email': f'{username}@test.com'
    }
    print(f"Registering user {username}...")
    resp = requests.post(f'{BASE_URL}/api/auth/signup', json=signup_payload)
    if resp.status_code != 200 and 'already exists' not in resp.text:
        print(f"Signup failed: {resp.text}")
        return None

    # Login
    login_payload = {'username': username, 'password': password}
    print(f"Logging in user {username}...")
    session = requests.Session()
    resp = session.post(f'{BASE_URL}/api/auth/login', json=login_payload)
    if resp.status_code != 200:
        print(f"Login failed: {resp.text}")
        return None
    
    return session

def upload_file(session, filename='test.txt'):
    files = {'file': (filename, 'dummy content')}
    print(f"Uploading {filename}...")
    resp = session.post(f'{BASE_URL}/upload', files=files)
    return resp

def main():
    username = 'limit_test_user_v2'
    password = 'password123'
    
    session = register_and_login(username, password)
    if not session:
        sys.exit(1)

    # Upload 3 files (should succeed)
    for i in range(1, 4):
        resp = upload_file(session, f'doc_{i}.txt')
        print(f"Upload {i}: Status {resp.status_code}")
        if resp.status_code != 200:
            print(f"Unexpected failure on upload {i}: {resp.text}")

    # Upload 4th file (should fail)
    print("Attempting 4th upload (should fail)...")
    resp = upload_file(session, 'doc_4.txt')
    print(f"Upload 4: Status {resp.status_code}")
    
    if resp.status_code == 403:
        print("SUCCESS: Limit enforced.")
    elif resp.status_code == 200:
        print("FAILURE: Limit NOT enforced.")
    else:
        print(f"Unexpected status: {resp.status_code} - {resp.text}")

if __name__ == '__main__':
    main()
