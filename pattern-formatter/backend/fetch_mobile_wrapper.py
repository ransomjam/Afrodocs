import urllib.request
import sys

url = "http://localhost:5000/mobile-pdf-viewer?file=https%3A%2F%2Fafrodocs.app%2Fdownload-pdf%2Fb40332a3-d741-4bc1-baf0-7310eb470a72%2Fdocument_20260123_formatted.pdf%3Finline%3Dtrue"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read()
        open("mobile_viewer_response.html", "wb").write(data)
        # Print head and tail
        head = data[:2000].decode('utf-8', 'replace')
        tail = data[-1000:].decode('utf-8', 'replace')
        print(head)
        print('\n---TAIL---\n')
        print(tail)
except Exception as e:
    print('ERROR', e)
    try:
        if hasattr(e, 'code'):
            print('HTTP code:', e.code)
    except Exception:
        pass
    sys.exit(1)
