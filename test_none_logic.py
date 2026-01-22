#!/usr/bin/env python3
"""
Test Python None handling to make sure logic is correct
"""

data = {
    'mergeJobId': None,
    'title': 'Test'
}

merge_job_id = data.get('mergeJobId')
print(f"merge_job_id = {merge_job_id}")
print(f"type = {type(merge_job_id)}")
print(f"bool(merge_job_id) = {bool(merge_job_id)}")

if merge_job_id:
    print("BRANCH: Merging")
else:
    print("BRANCH: Standalone")

# Also test without the key
data2 = {'title': 'Test'}
merge_job_id2 = data2.get('mergeJobId')
print(f"\nWith missing key:")
print(f"merge_job_id2 = {merge_job_id2}")
print(f"bool(merge_job_id2) = {bool(merge_job_id2)}")
