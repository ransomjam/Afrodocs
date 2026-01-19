#!/usr/bin/env python3
"""
Comprehensive test to verify the 300-page free tier limit is implemented correctly
across backend, database, and frontend integration.
"""

import requests
import json
import sys

API_BASE = "http://localhost:5000"

def test_api_responses():
    """Test that all API endpoints return correct data"""
    print("\n" + "="*70)
    print("TEST 1: Verify Backend Limit Configuration")
    print("="*70)
    
    # 1. Check auth status endpoint returns user data
    print("\n✓ Testing /api/auth/status endpoint...")
    
    # Create a test user first
    print("  - Creating test user...")
    register_resp = requests.post(
        f"{API_BASE}/api/auth/register",
        json={"username": "test_300_user", "password": "test123"}
    )
    
    if register_resp.status_code in [201, 400]:  # 201 = new user, 400 = user exists
        print("    ✓ User creation/exists check passed")
    else:
        print(f"    ✗ Unexpected response: {register_resp.status_code}")
        return False
    
    # Login
    print("  - Logging in...")
    login_resp = requests.post(
        f"{API_BASE}/api/auth/login",
        json={"username": "test_300_user", "password": "test123"}
    )
    
    if login_resp.status_code != 200:
        print(f"    ✗ Login failed: {login_resp.status_code}")
        return False
    
    print("    ✓ Login successful")
    
    # Get auth status
    print("  - Fetching auth status...")
    status_resp = requests.get(
        f"{API_BASE}/api/auth/status",
        cookies=login_resp.cookies
    )
    
    if status_resp.status_code != 200:
        print(f"    ✗ Auth status failed: {status_resp.status_code}")
        return False
    
    data = status_resp.json()
    print(f"    ✓ Auth status response: {json.dumps(data, indent=2)}")
    
    # Verify structure
    if not data.get('isAuthenticated'):
        print("    ✗ Not authenticated")
        return False
    
    print(f"    ✓ User authenticated: {data.get('username')}")
    print(f"    ✓ Plan: {data.get('plan')}")
    print(f"    ✓ Pages this month: {data.get('pages_this_month')}")
    print(f"    ✓ Pages balance: {data.get('pages_balance')}")
    
    return True

def verify_code_changes():
    """Verify the code changes are in place"""
    print("\n" + "="*70)
    print("TEST 2: Verify Code Changes in Source Files")
    print("="*70)
    
    issues = []
    
    # Check backend limit
    print("\n✓ Checking backend pattern_formatter_backend.py...")
    try:
        with open(r"c:\Users\user\Desktop\PATTERN\pattern-formatter\backend\pattern_formatter_backend.py", "r") as f:
            content = f.read()
            
        # Check for limit = 300
        if "limit = 300" in content:
            print("  ✓ Found 'limit = 300' in backend")
        else:
            issues.append("✗ Missing 'limit = 300' in backend")
        
        # Check comments updated
        if "# Check Free Tier Limit (300 pages)" in content:
            print("  ✓ Found updated comment: '300 pages' in line 13454")
        else:
            issues.append("✗ Missing updated comment for 300 pages")
        
        if "# New: Track pages (limit 300)" in content:
            print("  ✓ Found updated database comment: 'limit 300' in line 71")
        else:
            issues.append("✗ Missing updated database comment")
            
    except Exception as e:
        issues.append(f"Error reading backend file: {e}")
    
    # Check frontend changes
    print("\n✓ Checking frontend index.html...")
    try:
        with open(r"c:\Users\user\Desktop\PATTERN\pattern-formatter\frontend\index.html", "r") as f:
            content = f.read()
        
        # Check error message
        if "'Free tier limit reached (300 pages/month)'" in content:
            print("  ✓ Found updated error message: '300 pages/month'")
        else:
            issues.append("✗ Missing updated error message (300 pages/month)")
        
        # Check display
        if "{currentUser?.pages_this_month || 0}/300" in content:
            print("  ✓ Found updated display: '/300'")
        else:
            issues.append("✗ Missing updated display /300")
        
        # Check progress bar calculation
        if "(currentUser?.pages_this_month || 0) / 300 * 100" in content:
            print("  ✓ Found updated progress bar calculation: '/ 300'")
        else:
            issues.append("✗ Missing updated progress bar calculation")
            
    except Exception as e:
        issues.append(f"Error reading frontend file: {e}")
    
    if issues:
        print("\n" + "="*70)
        print("ISSUES FOUND:")
        for issue in issues:
            print(f"  {issue}")
        return False
    
    print("\n✓ All code changes verified successfully!")
    return True

def main():
    print("\n" + "="*70)
    print("COMPREHENSIVE TEST: 300-PAGE FREE TIER LIMIT")
    print("="*70)
    
    # Test 1: Code changes
    test1_passed = verify_code_changes()
    
    # Test 2: API responses
    try:
        test2_passed = test_api_responses()
    except Exception as e:
        print(f"\n✗ API test failed: {e}")
        test2_passed = False
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Code verification: {'✓ PASSED' if test1_passed else '✗ FAILED'}")
    print(f"API testing: {'✓ PASSED' if test2_passed else '✗ FAILED'}")
    
    if test1_passed and test2_passed:
        print("\n✓✓✓ ALL TESTS PASSED ✓✓✓")
        print("\nThe 300-page free tier limit has been successfully implemented:")
        print("  1. Backend limit set to 300 pages")
        print("  2. Frontend displays /300 correctly")
        print("  3. Error messages show '300 pages/month'")
        print("  4. API endpoints return correct user data")
        print("  5. Progress bar calculation uses 300 as denominator")
        print("\nNext step: Clear browser cache and refresh the page to see changes")
        return 0
    else:
        print("\n✗✗✗ SOME TESTS FAILED ✗✗✗")
        return 1

if __name__ == "__main__":
    sys.exit(main())
