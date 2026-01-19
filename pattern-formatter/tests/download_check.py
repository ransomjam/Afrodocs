import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
from pattern_formatter_backend import app, OUTPUT_FOLDER

client = app.test_client()

for job in ['test_1768136697005', 'test_1768136710399', 'c27487a3-5e3d-4dc7-afd7-3cdb91956e90']:
    resp = client.get(f'/download/{job}')
    print(job, '->', resp.status_code)
    try:
        print(resp.get_json())
    except Exception:
        print('Binary content or no JSON; length=', len(resp.data))
