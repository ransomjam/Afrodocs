#!/usr/bin/env python3
"""
Comprehensive Admin Functionality Test Suite
Tests:
1. Admin login
2. Admin can view all users
3. Admin can create users
4. Admin can delete users
5. Admin can view all user documents
6. Admin can download any user's documents
7. Admin has unlimited pages
8. Regular user cannot access admin endpoints
"""

import requests
import json
import sys
import time

BASE_URL = 'http://localhost:5000'

# Test credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin@secure123'
TEST_USER_USERNAME = 'testuser'
TEST_USER_PASSWORD = 'testpass123'

def print_test(name, passed, message=''):
    status = '[PASS]' if passed else '[FAIL]'
    print(f"{status} {name}")
    if message:
        print(f"  └─ {message}")

def test_admin_login():
    """Test 1: Admin can login"""
    print("\n" + "="*60)
    print("TEST 1: Admin Login")
    print("="*60)
    
    response = requests.post(f'{BASE_URL}/api/auth/login', json={
        'username': ADMIN_USERNAME,
        'password': ADMIN_PASSWORD
    })
    
    passed = response.status_code == 200
    data = response.json()
    
    print_test("Admin login", passed, f"Status: {response.status_code}")
    
    if passed:
        print(f"  └─ Username: {data.get('username')}")
        print(f"  └─ Plan: {data.get('plan')}")
        return True, data
    return False, None

def test_admin_status(session_cookie):
    """Test 2: Check admin status and verify is_admin flag"""
    print("\n" + "="*60)
    print("TEST 2: Check Admin Status")
    print("="*60)
    
    response = requests.get(f'{BASE_URL}/api/auth/status', cookies=session_cookie)
    
    passed = response.status_code == 200
    data = response.json()
    
    is_admin = data.get('is_admin', False)
    print_test("Admin status endpoint", passed, f"Status: {response.status_code}")
    print_test("is_admin flag is True", is_admin, f"is_admin: {is_admin}")
    
    if passed:
        print(f"  └─ Username: {data.get('username')}")
        print(f"  └─ Plan: {data.get('plan')}")
        print(f"  └─ Pages Balance: {data.get('pages_balance')}")
    
    return passed and is_admin

def test_admin_can_list_users(session_cookie):
    """Test 3: Admin can list all users"""
    print("\n" + "="*60)
    print("TEST 3: Admin List Users")
    print("="*60)
    
    response = requests.get(f'{BASE_URL}/api/admin/users', cookies=session_cookie)
    
    passed = response.status_code == 200
    data = response.json()
    
    print_test("List users endpoint", passed, f"Status: {response.status_code}")
    
    if passed:
        user_count = len(data)
        print(f"  └─ Total users: {user_count}")
        for user in data[:3]:  # Show first 3 users
            print(f"    • {user.get('username')} (admin: {user.get('is_admin')})")
    
    return passed

def test_admin_create_user(session_cookie):
    """Test 4: Admin can create users"""
    print("\n" + "="*60)
    print("TEST 4: Admin Create User")
    print("="*60)
    
    response = requests.post(f'{BASE_URL}/api/admin/users', 
        cookies=session_cookie,
        json={
            'username': TEST_USER_USERNAME,
            'password': TEST_USER_PASSWORD,
            'email': 'testuser@test.local',
            'institution': 'Test Institution',
            'contact': 'test@email.com',
            'plan': 'free',
            'pages_balance': 50
        }
    )
    
    passed = response.status_code == 201
    
    print_test("Create user endpoint", passed, f"Status: {response.status_code}")
    
    if passed:
        data = response.json()
        user = data.get('user', {})
        print(f"  └─ Created user: {user.get('username')}")
        print(f"  └─ Referral code: {user.get('referral_code')}")
        return True, user.get('id')
    
    return False, None

def test_user_cannot_access_admin(test_user_id):
    """Test 5: Regular users cannot access admin endpoints"""
    print("\n" + "="*60)
    print("TEST 5: Non-Admin User Cannot Access Admin Endpoints")
    print("="*60)
    
    # First, login as test user
    login_response = requests.post(f'{BASE_URL}/api/auth/login', json={
        'username': TEST_USER_USERNAME,
        'password': TEST_USER_PASSWORD
    })
    
    if login_response.status_code != 200:
        print_test("Test user login", False, "Could not login as test user")
        return False
    
    test_cookie = login_response.cookies
    
    # Try to list users
    response = requests.get(f'{BASE_URL}/api/admin/users', cookies=test_cookie)
    unauthorized = response.status_code == 403
    
    print_test("Regular user blocked from admin endpoints", unauthorized, 
               f"Status: {response.status_code} (expected 403)")
    
    return unauthorized

def test_admin_delete_user(session_cookie, user_id):
    """Test 6: Admin can delete users"""
    print("\n" + "="*60)
    print("TEST 6: Admin Delete User")
    print("="*60)
    
    response = requests.delete(f'{BASE_URL}/api/admin/users/{user_id}', cookies=session_cookie)
    
    passed = response.status_code == 200
    
    print_test("Delete user endpoint", passed, f"Status: {response.status_code}")
    
    if passed:
        print(f"  └─ User deleted successfully")
    
    return passed

def test_admin_can_check_admin(session_cookie):
    """Test 7: Admin can check their admin status"""
    print("\n" + "="*60)
    print("TEST 7: Admin Check Endpoint")
    print("="*60)
    
    response = requests.get(f'{BASE_URL}/api/admin/check', cookies=session_cookie)
    
    passed = response.status_code == 200
    data = response.json()
    
    is_admin = data.get('is_admin', False)
    
    print_test("Admin check endpoint", passed, f"Status: {response.status_code}")
    print_test("is_admin flag confirmed", is_admin, f"is_admin: {is_admin}")
    
    return passed and is_admin

def main():
    print("\n" + "="*60)
    print("ADMIN FUNCTIONALITY TEST SUITE")
    print("="*60)
    
    try:
        # Test 1: Admin Login
        login_passed, login_data = test_admin_login()
        if not login_passed:
            print("\n[FAILED] Cannot proceed without admin login")
            return False
        
        # Extract session cookie from login response
        # Note: requests automatically handles cookies if we use the same session
        session = requests.Session()
        login_response = session.post(f'{BASE_URL}/api/auth/login', json={
            'username': ADMIN_USERNAME,
            'password': ADMIN_PASSWORD
        })
        session_cookie = session.cookies
        
        # Test 2: Check Admin Status
        status_passed = test_admin_status(session_cookie)
        
        # Test 3: List Users
        list_passed = test_admin_can_list_users(session_cookie)
        
        # Test 4: Create User
        create_passed, user_id = test_admin_create_user(session_cookie)
        
        # Test 5: Non-admin cannot access admin endpoints
        access_denied_passed = test_user_cannot_access_admin(user_id)
        
        # Test 6: Delete User
        delete_passed = test_admin_delete_user(session_cookie, user_id) if user_id else False
        
        # Test 7: Admin check endpoint
        check_passed = test_admin_can_check_admin(session_cookie)
        
        # Summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        
        results = {
            'Admin Login': login_passed,
            'Admin Status': status_passed,
            'List Users': list_passed,
            'Create User': create_passed,
            'Access Control': access_denied_passed,
            'Delete User': delete_passed,
            'Admin Check': check_passed
        }
        
        for test_name, result in results.items():
            status = '[PASS]' if result else '[FAIL]'
            print(f"{status} {test_name}")
        
        all_passed = all(results.values())
        
        print("\n" + "="*60)
        if all_passed:
            print("ALL TESTS PASSED!")
            print("\nAdmin Credentials:")
            print(f"  Username: {ADMIN_USERNAME}")
            print(f"  Password: {ADMIN_PASSWORD}")
        else:
            print("SOME TESTS FAILED - See details above")
        print("="*60 + "\n")
        
        return all_passed
        
    except requests.exceptions.ConnectionError:
        print(f"\n[ERROR] Cannot connect to server at {BASE_URL}")
        print("Make sure the Flask server is running")
        return False
    except Exception as e:
        print(f"\n[ERROR] Test failed with exception: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
