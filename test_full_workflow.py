#!/usr/bin/env python3
"""
Comprehensive test of coverpage endpoint - both standalone and merge scenarios.
"""
import requests
import json
import time
import os
from pathlib import Path

BASE_URL = "http://localhost:5000"
session = requests.Session()

def print_section(title):
    print(f"\n{'='*70}")
    print(f"{title}")
    print(f"{'='*70}")

# Step 1: Login
print_section("STEP 1: AUTHENTICATE")

login_response = session.post(
    f"{BASE_URL}/api/auth/login",
    json={'username': 'admin', 'password': 'admin@secure123'},
    timeout=10
)

if login_response.status_code != 200:
    print(f"❌ Login failed: {login_response.text}")
    exit(1)

print(f"✅ Logged in as admin")

# Step 2: Generate standalone coverpage
print_section("STEP 2: GENERATE STANDALONE COVERPAGE")

coverpage_data = {
    'university': 'Bamenda',
    'documentType': 'Assignment',
    'studentName': 'Alice Mbuh',
    'studentId': 'MB24001234',
    'courseCode': 'CS301',
    'courseTitle': 'Software Engineering',
    'institution': 'College of Technology',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'level': '300 Level',
    'instructor': 'Prof. Nkengasong',
    'date': '2025-01-20',
    'title': 'Software Design Patterns'
}

response = session.post(
    f"{BASE_URL}/api/coverpage/generate",
    json=coverpage_data,
    timeout=30
)

if response.status_code != 200:
    print(f"❌ Failed to generate coverpage: {response.status_code}")
    print(f"   {response.text}")
    exit(1)

cover_result = response.json()
if not cover_result.get('success'):
    print(f"❌ Coverpage generation failed: {cover_result.get('error')}")
    exit(1)

cover_job_id = cover_result['job_id']
print(f"✅ Coverpage generated")
print(f"   Job ID: {cover_job_id}")
print(f"   Filename: {cover_result['filename']}")

# Download the coverpage
time.sleep(0.5)
download_response = session.get(
    f"{BASE_URL}/download/{cover_job_id}",
    timeout=30
)

if download_response.status_code != 200:
    print(f"❌ Failed to download coverpage")
    exit(1)

coverpage_path = Path(f"test_cover_{cover_job_id}.docx")
with open(coverpage_path, 'wb') as f:
    f.write(download_response.content)

print(f"✅ Coverpage downloaded: {len(download_response.content)} bytes")

# Step 3: Generate another document to test with (this would be the formatted document)
print_section("STEP 3: GENERATE CONTENT DOCUMENT")

# For now, we'll use the coverpage as the base document
content_data = {
    'university': 'Bamenda',
    'documentType': 'Assignment',
    'studentName': 'Alice Mbuh',
    'studentId': 'MB24001234',
    'courseCode': 'CS301',
    'courseTitle': 'Software Engineering',
    'institution': 'College of Technology',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'level': '300 Level',
    'instructor': 'Prof. Nkengasong',
    'date': '2025-01-20',
    'title': 'Software Design Patterns - Content'
}

response = session.post(
    f"{BASE_URL}/api/coverpage/generate",
    json=content_data,
    timeout=30
)

content_result = response.json()
if not content_result.get('success'):
    print(f"❌ Content generation failed: {content_result.get('error')}")
    exit(1)

content_job_id = content_result['job_id']
print(f"✅ Content document generated")
print(f"   Job ID: {content_job_id}")

# Step 4: Now merge coverpage with content
print_section("STEP 4: MERGE COVERPAGE WITH CONTENT")

merge_data = {
    'university': 'Bamenda',
    'documentType': 'Assignment',
    'studentName': 'Alice Mbuh',
    'studentId': 'MB24001234',
    'courseCode': 'CS301',
    'courseTitle': 'Software Engineering',
    'institution': 'College of Technology',
    'faculty': 'College of Technology',
    'department': 'Computer Engineering',
    'level': '300 Level',
    'instructor': 'Prof. Nkengasong',
    'date': '2025-01-20',
    'title': 'Software Design Patterns',
    'mergeJobId': content_job_id  # KEY FIELD: This triggers merge
}

response = session.post(
    f"{BASE_URL}/api/coverpage/generate",
    json=merge_data,
    timeout=30
)

if response.status_code != 200:
    print(f"❌ Merge failed: {response.status_code}")
    print(f"   {response.text}")
    exit(1)

merge_result = response.json()
if not merge_result.get('success'):
    print(f"❌ Merge generation failed: {merge_result.get('error')}")
    exit(1)

merge_job_id = merge_result['job_id']
print(f"✅ Merge completed")
print(f"   Returned Job ID: {merge_job_id}")
print(f"   Is Merged: {merge_result.get('is_merged')}")
print(f"   Merged From: {merge_result.get('merged_from')}")
print(f"   Filename: {merge_result['filename']}")

# Step 5: Download merged document
print_section("STEP 5: DOWNLOAD MERGED DOCUMENT")

time.sleep(0.5)
download_response = session.get(
    f"{BASE_URL}/download/{merge_job_id}",
    timeout=30
)

if download_response.status_code != 200:
    print(f"❌ Failed to download merged document: {download_response.status_code}")
    print(f"   {download_response.text[:200]}")
    exit(1)

merged_path = Path(f"test_merged_{merge_job_id}.docx")
with open(merged_path, 'wb') as f:
    f.write(download_response.content)

print(f"✅ Merged document downloaded: {len(download_response.content)} bytes")

# Summary
print_section("TEST SUMMARY")
print(f"✅ All tests passed!")
print(f"   Standalone Coverpage Job ID: {cover_job_id}")
print(f"   Content Document Job ID: {content_job_id}")
print(f"   Merged Document Job ID: {merge_job_id}")
print(f"   Downloaded files:")
print(f"     - {coverpage_path.name}")
print(f"     - {merged_path.name}")

# Cleanup
print(f"\nCleaning up test files...")
if coverpage_path.exists():
    coverpage_path.unlink()
if merged_path.exists():
    merged_path.unlink()

print(f"✅ Complete!")
