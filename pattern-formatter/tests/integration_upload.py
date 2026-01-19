import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
from pattern_formatter_backend import app, OUTPUT_FOLDER

client = app.test_client()

# Reset usage to be safe
print('Resetting usage...')
r = client.get('/debug/reset_usage/all')
print('reset:', r.status_code, r.get_json())

# Create a test user
print('Signing up test user...')
resp = client.post('/api/auth/signup', json={'username': 'integration_test', 'password': 'pass123'})
print('signup:', resp.status_code, resp.get_json())

# Login
print('Logging in test user...')
resp = client.post('/api/auth/login', json={'username': 'integration_test', 'password': 'pass123'})
print('login:', resp.status_code, resp.get_json())

# Prepare sample file
sample = os.path.join(os.path.dirname(__file__), 'sample_academic_paper.txt')
if not os.path.exists(sample):
    print('Sample file missing:', sample)
    sys.exit(1)

print('Uploading file...')
with open(sample, 'rb') as f:
    data = {'file': (f, 'sample_academic_paper.txt')}
    resp = client.post('/upload', content_type='multipart/form-data', data=data)
    print('upload status:', resp.status_code)
    try:
        print('response json:', resp.get_json())
    except Exception:
        print('No JSON; raw length=', len(resp.data))

# If successful, attempt download
if resp.status_code == 200:
    job_id = resp.get_json().get('job_id')
    print('Job id:', job_id)
    dl = client.get(f'/download/{job_id}')
    print('download status:', dl.status_code)
    if dl.status_code == 200:
        out_file = os.path.join(os.getcwd(), f'{job_id}_download.docx')
        with open(out_file, 'wb') as fh:
            fh.write(dl.data)
        print('Saved download to', out_file)
