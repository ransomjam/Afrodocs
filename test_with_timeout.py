#!/usr/bin/env python
import sys
import os
import threading
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pattern-formatter', 'backend'))

result_container = {'result': None, 'error': None, 'done': False}

def process_with_timeout():
    try:
        from pattern_formatter_backend import DocumentProcessor
        print('1. Import successful')

        processor = DocumentProcessor()
        print('2. Processor created')

        result = processor.process_docx('Samples/Sample with Certification.docx')
        print('3. Processing successful!')
        result_container['result'] = result
    except Exception as e:
        print(f'Error: {type(e).__name__}: {e}')
        result_container['error'] = e
        import traceback
        traceback.print_exc()
    finally:
        result_container['done'] = True

# Start processing in a thread
thread = threading.Thread(target=process_with_timeout, daemon=False)
thread.start()

# Wait for up to 30 seconds
thread.join(timeout=30)

if thread.is_alive():
    print('TIMEOUT: Processing took longer than 30 seconds')
    # Note: Can't actually kill the thread on Windows, but we can exit
    sys.exit(1)
elif result_container['done']:
    if result_container['error']:
        sys.exit(1)
    else:
        print('Success!')
