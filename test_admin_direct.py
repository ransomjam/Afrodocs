#!/usr/bin/env python3
"""
Test admin functionality directly with database
"""

import sys
import os

# Add backend to path
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import app, db, User
from werkzeug.security import check_password_hash

def test_admin_account():
    """Test that admin account was created with correct properties"""
    print("\n" + "="*60)
    print("DIRECT DATABASE ADMIN TESTS")
    print("="*60 + "\n")
    
    with app.app_context():
        # Test 1: Admin account exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("[FAIL] Admin account not found in database")
            return False
        
        print("[PASS] Admin account exists")
        print(f"  └─ Username: {admin.username}")
        print(f"  └─ Email: {admin.email}")
        print(f"  └─ is_admin: {admin.is_admin}")
        
        # Test 2: Admin has is_admin flag set
        if not admin.is_admin:
            print("[FAIL] Admin account is_admin flag is False")
            return False
        print("[PASS] Admin is_admin flag is True")
        
        # Test 3: Password is correct
        if not check_password_hash(admin.password_hash, 'admin@secure123'):
            print("[FAIL] Admin password is incorrect")
            return False
        print("[PASS] Admin password is correct")
        
        # Test 4: Admin has unlimited pages
        if admin.pages_balance != 999999:
            print(f"[FAIL] Admin pages_balance is {admin.pages_balance}, expected 999999")
            return False
        print("[PASS] Admin has unlimited pages (999999)")
        
        # Test 5: Admin plan is enterprise
        if admin.plan != 'enterprise':
            print(f"[FAIL] Admin plan is '{admin.plan}', expected 'enterprise'")
            return False
        print("[PASS] Admin plan is set to 'enterprise'")
        
        # Test 6: Create test user
        test_user = User(
            username='test_user_direct',
            password_hash='testhash',
            email='test@test.local',
            is_admin=False,
            plan='free'
        )
        db.session.add(test_user)
        db.session.commit()
        print("[PASS] Test user created successfully")
        
        # Test 7: Verify test user doesn't have admin privileges
        if test_user.is_admin:
            print("[FAIL] Test user should not have admin privileges")
            db.session.delete(test_user)
            db.session.commit()
            return False
        print("[PASS] Test user correctly has is_admin=False")
        
        # Test 8: List all users
        all_users = User.query.all()
        print(f"[PASS] Database contains {len(all_users)} users:")
        for user in all_users:
            print(f"  • {user.username} (admin: {user.is_admin}, plan: {user.plan})")
        
        # Clean up test user
        db.session.delete(test_user)
        db.session.commit()
        print("[PASS] Test user deleted")
        
        # Test 9: Admin can create users (just verify the User model works)
        new_user = User(
            username='newuser_test',
            password_hash='hashed_pass',
            email='new@test.local',
            institution='Test Institution',
            contact='contact@test.local',
            is_admin=False,
            plan='free',
            pages_balance=50
        )
        db.session.add(new_user)
        db.session.commit()
        print("[PASS] New user creation works (user: newuser_test)")
        
        # Verify new user exists
        created_user = User.query.filter_by(username='newuser_test').first()
        if not created_user:
            print("[FAIL] New user was not saved to database")
            return False
        print("[PASS] New user verified in database")
        
        # Clean up
        db.session.delete(created_user)
        db.session.commit()
        
        print("\n" + "="*60)
        print("ALL ADMIN TESTS PASSED!")
        print("="*60)
        print("\nAdmin Credentials:")
        print(f"  Username: admin")
        print(f"  Password: admin@secure123")
        print(f"  Email: admin@formatter.local")
        print(f"  Plan: {admin.plan}")
        print(f"  Pages: {admin.pages_balance} (unlimited)")
        print("="*60 + "\n")
        
        return True

if __name__ == '__main__':
    try:
        success = test_admin_account()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
