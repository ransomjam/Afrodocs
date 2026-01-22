#!/usr/bin/env python3
"""
Comprehensive test for payment, tiers, and referrals systems
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"
SESSION = requests.Session()

def test_auth_flow():
    """Test authentication flow"""
    print("\n=== Testing Auth Flow ===")
    
    # Test signup
    print("\n1. Testing SIGNUP")
    signup_data = {
        "username": f"testuser_{datetime.now().timestamp()}",
        "password": "SecurePass123!",
        "email": f"test_{datetime.now().timestamp()}@example.com",
        "institution": "Test University",
        "contact": "+1234567890"
    }
    
    r = SESSION.post(f"{BASE_URL}/api/auth/signup", json=signup_data)
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    if r.status_code != 201:
        print("   ❌ Signup failed!")
        return False
    
    signup_response = r.json()
    referral_code = signup_response.get('referral_code')
    print(f"   ✓ Signup successful! Referral code: {referral_code}")
    
    # Test login
    print("\n2. Testing LOGIN")
    login_data = {
        "username": signup_data["username"],
        "password": signup_data["password"]
    }
    
    r = SESSION.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    if r.status_code != 200:
        print("   ❌ Login failed!")
        return False
    
    print("   ✓ Login successful!")
    
    # Test auth status
    print("\n3. Testing AUTH STATUS")
    r = SESSION.get(f"{BASE_URL}/api/auth/status")
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    if r.status_code != 200 or not r.json().get('isAuthenticated'):
        print("   ❌ Auth status check failed!")
        return False
    
    print("   ✓ Auth status check successful!")
    
    return {
        'username': signup_data['username'],
        'email': signup_data['email'],
        'referral_code': referral_code
    }

def test_payment_initiation(user_info):
    """Test payment initiation"""
    print("\n=== Testing Payment Initiation ===")
    
    amounts_to_test = [100, 250, 500]
    
    for amount in amounts_to_test:
        print(f"\n1. Testing payment initiation for {amount} XAF")
        
        payment_data = {
            "amount": amount
        }
        
        r = SESSION.post(f"{BASE_URL}/api/payment/initiate", json=payment_data)
        print(f"   Status: {r.status_code}")
        response = r.json()
        print(f"   Response: {json.dumps(response, indent=2)}")
        
        if r.status_code != 200:
            print(f"   ❌ Payment initiation failed for {amount} XAF")
        else:
            print(f"   ✓ Payment initiation successful for {amount} XAF")
            
            # Check if payment link/transId returned
            if response.get('link') or response.get('transId'):
                print(f"   ✓ Payment gateway link/transId provided")
            else:
                print(f"   ⚠ No payment link/transId in response")

def test_tier_system(user_info):
    """Test tier system"""
    print("\n=== Testing Tier System ===")
    
    print("\n1. Checking user plan after registration")
    r = SESSION.get(f"{BASE_URL}/api/auth/status")
    user_data = r.json()
    
    print(f"   User Plan: {user_data.get('plan')}")
    print(f"   Pages Balance: {user_data.get('pages_balance')}")
    print(f"   Pages This Month: {user_data.get('pages_this_month')}")
    
    if user_data.get('plan') != 'free':
        print(f"   ❌ New users should start with 'free' plan, got '{user_data.get('plan')}'")
    else:
        print(f"   ✓ New user has correct plan: free")

def test_referral_system():
    """Test referral system"""
    print("\n=== Testing Referral System ===")
    
    # Create a referrer user
    print("\n1. Creating referrer user")
    referrer_data = {
        "username": f"referrer_{datetime.now().timestamp()}",
        "password": "SecurePass123!",
        "email": f"referrer_{datetime.now().timestamp()}@example.com",
        "institution": "Test University",
        "contact": "+1234567890"
    }
    
    r = SESSION.post(f"{BASE_URL}/api/auth/signup", json=referrer_data)
    referrer_response = r.json()
    referral_code = referrer_response.get('referral_code')
    
    print(f"   Referrer referral code: {referral_code}")
    
    # Get referrer's initial balance
    r = SESSION.get(f"{BASE_URL}/api/auth/status")
    referrer_initial_balance = r.json().get('pages_balance', 0)
    print(f"   Referrer initial balance: {referrer_initial_balance}")
    
    # Create a referred user
    print("\n2. Creating referred user with referral code")
    SESSION.cookies.clear()  # Clear session for new user
    
    referred_data = {
        "username": f"referred_{datetime.now().timestamp()}",
        "password": "SecurePass123!",
        "email": f"referred_{datetime.now().timestamp()}@example.com",
        "institution": "Test University",
        "contact": "+1234567890",
        "referral_code": referral_code
    }
    
    r = SESSION.post(f"{BASE_URL}/api/auth/signup", json=referred_data)
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    if r.status_code != 201:
        print("   ❌ Referred user signup failed!")
        return
    
    print("   ✓ Referred user created successfully!")
    
    # Check referred user got initial pages
    referred_response = r.json()
    r = SESSION.post(f"{BASE_URL}/api/auth/login", json={
        "username": referred_data["username"],
        "password": referred_data["password"]
    })
    
    referred_user_data = SESSION.get(f"{BASE_URL}/api/auth/status").json()
    referred_initial_balance = referred_user_data.get('pages_balance', 0)
    
    print(f"\n3. Checking rewards")
    print(f"   Referred user initial balance: {referred_initial_balance}")
    
    if referred_initial_balance > 0:
        print(f"   ✓ Referred user got initial reward: {referred_initial_balance} pages")
    else:
        print(f"   ❌ Referred user should have initial reward")

def test_payment_verification():
    """Test payment verification"""
    print("\n=== Testing Payment Verification ===")
    
    print("\n1. Testing verify-pending endpoint")
    r = SESSION.post(f"{BASE_URL}/api/payment/verify-pending")
    print(f"   Status: {r.status_code}")
    print(f"   Response: {r.json()}")
    
    if r.status_code == 200:
        print("   ✓ Payment verification endpoint working")
    else:
        print("   ❌ Payment verification endpoint failed")

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("AFRODOCS PAYMENT, TIERS & REFERRALS TEST SUITE")
    print("=" * 60)
    
    # Test auth flow
    user_info = test_auth_flow()
    if not user_info:
        print("\n❌ Auth flow test failed. Cannot continue.")
        return
    
    # Test tier system
    test_tier_system(user_info)
    
    # Test payment
    test_payment_initiation(user_info)
    
    # Test payment verification
    test_payment_verification()
    
    # Test referral system
    test_referral_system()
    
    print("\n" + "=" * 60)
    print("TEST SUITE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()
