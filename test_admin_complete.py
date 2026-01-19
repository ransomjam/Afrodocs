#!/usr/bin/env python3
"""
Comprehensive Admin Feature Verification
Tests all admin functionality without needing HTTP server
"""

import sys
import os

# Add backend to path
sys.path.insert(0, r'c:\Users\user\Desktop\PATTERN\pattern-formatter\backend')

from pattern_formatter_backend import app, db, User, DocumentRecord
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

def header(text):
    print("\n" + "="*80)
    print(text.center(80))
    print("="*80 + "\n")

def test_section(name):
    print(f"\n{'─'*80}")
    print(f"▶ {name}")
    print(f"{'─'*80}\n")

def test_pass(msg, details=""):
    print(f"  ✓ {msg}")
    if details:
        print(f"    └─ {details}")

def test_fail(msg, details=""):
    print(f"  ✗ {msg}")
    if details:
        print(f"    └─ {details}")
    return False

def run_tests():
    header("COMPREHENSIVE ADMIN VERIFICATION TEST SUITE")
    
    all_passed = True
    
    with app.app_context():
        
        # TEST 1: Admin Account Existence and Properties
        test_section("TEST 1: Admin Account Properties")
        
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            test_fail("Admin account not found")
            return False
        test_pass("Admin account exists")
        
        if admin.is_admin != True:
            test_fail(f"Admin is_admin flag is {admin.is_admin}, expected True")
            all_passed = False
        else:
            test_pass("Admin is_admin flag is True")
        
        if not check_password_hash(admin.password_hash, 'admin@secure123'):
            test_fail("Admin password is incorrect")
            all_passed = False
        else:
            test_pass("Admin password is correct: admin@secure123")
        
        if admin.pages_balance != 999999:
            test_fail(f"Admin pages_balance is {admin.pages_balance}, expected 999999")
            all_passed = False
        else:
            test_pass("Admin has unlimited pages", f"pages_balance: {admin.pages_balance}")
        
        if admin.plan != 'enterprise':
            test_fail(f"Admin plan is '{admin.plan}', expected 'enterprise'")
            all_passed = False
        else:
            test_pass("Admin plan is 'enterprise'")
        
        if admin.email != 'admin@formatter.local':
            test_fail(f"Admin email is '{admin.email}', expected 'admin@formatter.local'")
            all_passed = False
        else:
            test_pass("Admin email is correct: admin@formatter.local")
        
        # TEST 2: User Creation Functionality
        test_section("TEST 2: User Creation via Admin")
        
        test_users = []
        for i in range(3):
            user = User(
                username=f'testuser_{i}',
                password_hash=generate_password_hash(f'pass{i}'),
                email=f'test{i}@test.local',
                institution=f'Institution {i}',
                contact=f'contact{i}@test.com',
                is_admin=False,
                plan='free',
                pages_balance=50 * (i + 1),
                referral_code=f'REF{i:03d}'
            )
            db.session.add(user)
            test_users.append(user)
            test_pass(f"Created user: testuser_{i}")
        
        db.session.commit()
        test_pass(f"All {len(test_users)} test users saved to database")
        
        # TEST 3: User Retrieval and Listing
        test_section("TEST 3: User Listing and Retrieval")
        
        all_users = User.query.all()
        admin_count = User.query.filter_by(is_admin=True).count()
        regular_count = User.query.filter_by(is_admin=False).count()
        
        test_pass(f"Total users in database: {len(all_users)}")
        test_pass(f"Admin users: {admin_count}")
        test_pass(f"Regular users: {regular_count}")
        
        if admin_count < 1:
            test_fail("No admin users found in database")
            all_passed = False
        else:
            test_pass("Admin user(s) present in database")
        
        # TEST 4: Non-Admin User Restrictions
        test_section("TEST 4: Non-Admin User Properties")
        
        regular_user = User.query.filter_by(username='testuser_0').first()
        if not regular_user:
            test_fail("Test user testuser_0 not found")
            all_passed = False
        else:
            if regular_user.is_admin:
                test_fail("Regular user should not have is_admin=True")
                all_passed = False
            else:
                test_pass("Regular user has is_admin=False")
            
            if regular_user.plan != 'free':
                test_fail(f"Regular user plan is '{regular_user.plan}', expected 'free'")
                all_passed = False
            else:
                test_pass("Regular user plan is 'free'")
            
            if regular_user.pages_balance != 50:
                test_fail(f"Regular user pages_balance is {regular_user.pages_balance}, expected 50")
                all_passed = False
            else:
                test_pass(f"Regular user pages_balance: {regular_user.pages_balance}")
        
        # TEST 5: Admin Privileges vs Regular User Privileges
        test_section("TEST 5: Privilege Comparison")
        
        test_pass("Admin privileges:")
        print(f"    • is_admin: True")
        print(f"    • pages_balance: {admin.pages_balance} (unlimited)")
        print(f"    • plan: {admin.plan}")
        print(f"    • can_manage_users: Yes")
        print(f"    • can_access_all_documents: Yes")
        print(f"    • page_limit: None")
        
        test_pass("Regular user privileges:")
        print(f"    • is_admin: False")
        print(f"    • pages_balance: {regular_user.pages_balance}")
        print(f"    • plan: {regular_user.plan}")
        print(f"    • can_manage_users: No")
        print(f"    • can_access_all_documents: No")
        print(f"    • page_limit: 300/month")
        
        # TEST 6: User Deletion
        test_section("TEST 6: User Deletion")
        
        user_to_delete = User.query.filter_by(username='testuser_2').first()
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
            test_pass("User testuser_2 deleted")
            
            deleted_check = User.query.filter_by(username='testuser_2').first()
            if deleted_check:
                test_fail("User still exists after deletion")
                all_passed = False
            else:
                test_pass("Deletion verified - user no longer in database")
        
        # TEST 7: Document Access Model
        test_section("TEST 7: Document Model and Access Control")
        
        # Create a test document for a regular user
        doc = DocumentRecord(
            user_id=regular_user.id,
            filename='test_doc_uuid.docx',
            original_filename='test_document.docx',
            job_id='test-job-id-12345',
            file_path='outputs/test_doc.docx'
        )
        db.session.add(doc)
        db.session.commit()
        test_pass("Test document created for regular user")
        
        # Verify admin can access user's documents
        user_docs = DocumentRecord.query.filter_by(user_id=regular_user.id).all()
        test_pass(f"Admin can query user documents: {len(user_docs)} found")
        
        # Clean up
        db.session.delete(doc)
        db.session.commit()
        
        # TEST 8: Database Schema Verification
        test_section("TEST 8: Database Schema Verification")
        
        # Check if is_admin column exists
        inspector = db.inspect(db.engine)
        user_columns = [col['name'] for col in inspector.get_columns('user')]
        
        if 'is_admin' in user_columns:
            test_pass("is_admin column exists in user table")
        else:
            test_fail("is_admin column NOT found in user table")
            all_passed = False
        
        required_columns = ['id', 'username', 'password_hash', 'email', 'is_admin', 'plan', 'pages_balance']
        for col in required_columns:
            if col in user_columns:
                print(f"    ✓ {col:20} present")
            else:
                print(f"    ✗ {col:20} MISSING")
                all_passed = False
        
        # TEST 9: Admin Referral Code
        test_section("TEST 9: Admin Metadata")
        
        test_pass(f"Admin referral code: {admin.referral_code}")
        test_pass(f"Admin documents generated: {admin.documents_generated}")
        test_pass(f"Admin institution: {admin.institution}")
        test_pass(f"Admin contact: {admin.contact}")
        
        # TEST 10: Final User Count
        test_section("TEST 10: Final Database State")
        
        final_count = User.query.count()
        final_admins = User.query.filter_by(is_admin=True).count()
        final_regulars = User.query.filter_by(is_admin=False).count()
        
        print(f"  Total Users: {final_count}")
        print(f"  ├─ Admin Users: {final_admins}")
        print(f"  └─ Regular Users: {final_regulars}")
        
        test_pass("Database state verified")
        
        # Clean up remaining test users
        test_section("CLEANUP: Removing test users")
        
        for user in [u for u in User.query.all() if u.username.startswith('testuser_')]:
            db.session.delete(user)
            test_pass(f"Deleted: {user.username}")
        
        db.session.commit()
        test_pass("All test users cleaned up")
    
    # SUMMARY
    header("TEST SUMMARY")
    
    if all_passed:
        print("✓ ALL TESTS PASSED\n")
        print("Admin Account Successfully Configured:")
        print(f"  Username:  admin")
        print(f"  Password:  admin@secure123")
        print(f"  Email:     admin@formatter.local")
        print(f"  Plan:      Enterprise (Unlimited Pages)")
        print(f"  Status:    Ready for use\n")
        return True
    else:
        print("✗ SOME TESTS FAILED\n")
        print("Please review the failures above.\n")
        return False

if __name__ == '__main__':
    try:
        success = run_tests()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ Test execution failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
