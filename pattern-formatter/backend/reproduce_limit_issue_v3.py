import requests
import sys
import os

BASE_URL = 'http://localhost:5000'

def register(username, password):
    url = f"{BASE_URL}/api/auth/signup"
    data = {
        "username": username,
        "password": password,
        "institution": "Test Inst",
        "email": f"{username}@test.com"
    }
    response = requests.post(url, json=data)
    return response

def login(username, password):
    url = f"{BASE_URL}/api/auth/login"
    data = {"username": username, "password": password}
    session = requests.Session()
    response = session.post(url, json=data)
    if response.status_code == 200:
        return session
    return None

def upload_file(session, filename="test.txt"):
    url = f"{BASE_URL}/upload"
    with open(filename, 'w') as f:
        f.write("Test content")
    
    with open(filename, 'rb') as f:
        files = {'file': f}
        response = session.post(url, files=files)
    return response

def test_limit():
    username = "limit_test_user_v3"
    password = "password123"
    
    print(f"Registering {username}...")
    reg_res = register(username, password)
    if reg_res.status_code != 200 and "already exists" not in reg_res.text:
        print(f"Registration failed: {reg_res.text}")
        return

    print("Logging in...")
    session = login(username, password)
    if not session:
        print("Login failed")
        return

    print("Uploading 3 documents (should succeed)...")
    for i in range(3):
        res = upload_file(session)
        print(f"Upload {i+1}: {res.status_code}")
        if res.status_code != 200:
            print(f"Unexpected failure on upload {i+1}: {res.text}")
            return

    print("Uploading 4th document (should fail)...")
    res = upload_file(session)
    print(f"Upload 4: {res.status_code}")
    
    if res.status_code == 403:
        print("SUCCESS: Limit enforced.")
    else:
        print(f"FAILURE: Limit NOT enforced. Status: {res.status_code}")

if __name__ == "__main__":
    try:
        test_limit()
    except Exception as e:
        print(f"Error: {e}")
