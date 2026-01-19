import requests
import io

session = requests.Session()

print("Testing authentication flow...")
print("=" * 50)

# Test signup first (in case user doesn't exist)
signup_resp = session.post('http://localhost:5000/api/auth/signup', json={'username': 'testuser999', 'password': 'test123'})
print(f'Signup: {signup_resp.status_code} - {signup_resp.json()}')

# Test login
login_resp = session.post('http://localhost:5000/api/auth/login', json={'username': 'testuser999', 'password': 'test123'})
print(f'Login: {login_resp.status_code} - {login_resp.json()}')

# Check cookies
print(f'Session cookies: {dict(session.cookies)}')

# Test auth status
status_resp = session.get('http://localhost:5000/api/auth/status')
print(f'Status: {status_resp.status_code} - {status_resp.json()}')

# Test upload with a simple text file
print("=" * 50)
print("Testing upload...")
files = {'file': ('test.txt', io.BytesIO(b'CHAPTER ONE Introduction This is some body text for testing the document formatter.'), 'text/plain')}
upload_resp = session.post('http://localhost:5000/upload', files=files)
print(f'Upload: {upload_resp.status_code}')
if upload_resp.status_code == 200:
    print(f'Upload Success: {upload_resp.json().get("message", "OK")}')
else:
    print(f'Upload Failed: {upload_resp.text[:500]}')

print("=" * 50)
print("Test complete!")
