# AfroDocs Launch Checklist

## ✅ Payment, Tiers & Referrals Status

### Payment System
| Feature | Status | Notes |
|---------|--------|-------|
| Payment initiation endpoint | ✅ Ready | Requires Fapshi API key |
| Payment verification | ✅ Ready | Works correctly |
| Payment webhook | ✅ Ready | Handles callbacks from Fapshi |
| Error handling | ✅ Fixed | Returns 503 when API not configured |
| Frontend payment button | ✅ Fixed | Added credentials: 'include' |

### Tier System  
| Tier | Amount (XAF) | Pages | Status |
|------|--------------|-------|--------|
| Free | 0 | 0 | ✅ Default for new users |
| Student | 100 | 500 | ✅ Configured |
| Campus Pro | 250 | 1,500 | ✅ Configured |
| Enterprise | 500 | 10,000 | ✅ Configured |
| Custom | Variable | 50 per 100 XAF | ✅ Fallback |

### Referral System
| Feature | Status | Reward |
|---------|--------|--------|
| Referral code generation | ✅ Working | Unique 8-char code |
| Signup bonus (referred user) | ✅ Working | 50 pages |
| Signup bonus (referrer) | ✅ Working | 50 pages |
| Payment bonus (referrer) | ✅ Ready | 10% of referred user's pages |
| Max referral rewards | ✅ Configured | 100 rewards per user |

---

## 🔧 Configuration Required Before Launch

### 1. Fapshi Payment Gateway API Key

**CRITICAL**: Set these environment variables:

```bash
# Windows PowerShell
$env:FAPSHI_API_USER = "c02a978a-5e79-4b8e-9906-32847acaacc5"
$env:FAPSHI_API_KEY = "YOUR_FAPSHI_API_KEY_HERE"

# Linux/Mac
export FAPSHI_API_USER="c02a978a-5e79-4b8e-9906-32847acaacc5"
export FAPSHI_API_KEY="YOUR_FAPSHI_API_KEY_HERE"
```

Get your API key from: https://dashboard.fapshi.com/

### 2. Flask Secret Key

Change the secret key in production:

```python
# In pattern_formatter_backend.py
app.config['SECRET_KEY'] = 'generate-a-secure-random-key-here'
```

Generate a secure key:
```python
import secrets
print(secrets.token_hex(32))
```

### 3. Production Cookie Settings

Update in `pattern_formatter_backend.py`:
```python
app.config['SESSION_COOKIE_SECURE'] = True  # Enable for HTTPS
app.config['REMEMBER_COOKIE_SECURE'] = True  # Enable for HTTPS
```

### 4. CORS Origins

Update for production domain:
```python
CORS(app, origins=["https://yourdomain.com"])
```

---

## 📋 Pre-Launch Verification Checklist

### Authentication
- [ ] User signup works
- [ ] User login works
- [ ] Session persistence works
- [ ] Logout works
- [ ] Admin login works (admin / admin@secure123)

### Payments
- [ ] Fapshi API key configured
- [ ] Test payment with 100 XAF (Student plan)
- [ ] Test payment with 250 XAF (Campus Pro plan)
- [ ] Test payment with 500 XAF (Enterprise plan)
- [ ] Verify pages added to account after payment
- [ ] Verify plan upgrade after payment

### Referrals
- [ ] Test referral signup flow
- [ ] Verify referrer gets 50 pages bonus
- [ ] Verify referred user gets 50 pages bonus
- [ ] Verify referrer gets 10% bonus when referred user pays

### Document Processing
- [ ] File upload works
- [ ] Document formatting works
- [ ] Download works (DOCX & PDF)
- [ ] Cover page generation works

---

## 🚀 Deployment Steps

1. **Set environment variables** (see above)

2. **Start the server**:
   ```bash
   cd pattern-formatter/backend
   python pattern_formatter_backend.py
   ```

3. **For production**, use a WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 pattern_formatter_backend:app
   ```

4. **Verify health check**:
   ```bash
   curl http://localhost:5000/health
   ```
   
   Expected response:
   ```json
   {
     "status": "healthy",
     "payment_service": "configured",
     ...
   }
   ```

---

## 📁 Files Modified

| File | Changes |
|------|---------|
| `fapshi_integration.py` | Added API key validation, better error messages |
| `pattern_formatter_backend.py` | Centralized pricing tiers, improved payment handling, referral bonuses on payment |
| `frontend/index.html` | Fixed handleUpgrade to include credentials and API_BASE |
| `.env.example` | Created template for environment variables |

---

## 🐛 Known Issues Fixed

1. **401 on Payment**: Fixed by adding `credentials: 'include'` to fetch calls
2. **Missing API key error**: Now returns user-friendly 503 error
3. **Inconsistent payment logic**: Centralized in `apply_successful_payment()` function
4. **Referrer not rewarded on payment**: Added 10% bonus logic

---

## 📞 Support

For issues with the payment gateway, contact Fapshi support at https://fapshi.com/

For app issues, check the server logs:
```bash
tail -f backend.log
```
