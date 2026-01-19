import requests
import time

BASE_URL = 'http://localhost:5000'

def test_limit():
    # 1. Signup
    username = f"test_user_{int(time.time())}"
    password = "password123"
    session = requests.Session()
    
    print(f"Creating user {username}...")
    resp = session.post(f"{BASE_URL}/api/auth/signup", json={
        "username": username,
        "password": password,
        "email": f"{username}@example.com"
    })
    if resp.status_code != 200:
        print("Signup failed:", resp.text)
        return

    # 2. Login (Signup usually logs in, but let's be sure)
    resp = session.post(f"{BASE_URL}/api/auth/login", json={
        "username": username,
        "password": password
    })
    if resp.status_code != 200:
        print("Login failed:", resp.text)
        return
    
    print("Logged in.")

    # 3. Upload 4 files
    for i in range(1, 6):
        print(f"Uploading file {i}...")
        files = {'file': ('test.txt', b'Sample content')}
        resp = session.post(f"{BASE_URL}/upload", files=files)
        
        print(f"Response {i}: {resp.status_code}")
        if resp.status_code == 403:
            print("Limit reached as expected!")
            break
        elif resp.status_code != 200:
            print("Upload failed:", resp.text)
        else:
            print("Upload successful.")

if __name__ == "__main__":
    test_limit()
