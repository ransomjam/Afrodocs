import re
import requests
import os
import logging

# Load .env file if it exists
try:
    from dotenv import load_dotenv
    # Load from .env file in the same directory
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    load_dotenv(env_path)
except ImportError:
    pass  # python-dotenv not installed, rely on environment variables

logger = logging.getLogger(__name__)

# Configuration - Production Mode
# API credentials should be set via environment variables
BASE_URL = 'https://live.fapshi.com'
API_USER = os.environ.get('FAPSHI_API_USER', '172eaf6b-8104-4b46-83fe-07e8a943d695')
API_KEY = os.environ.get('FAPSHI_API_KEY', 'FAK_72d40a861aeb1a075c48f8a4833a6af3')

HEADERS = {
    'apiuser': API_USER,
    'apikey': API_KEY
}

ERRORS = [
    'invalid type, string expected',
    'invalid type, dictionary expected',
    'amount required',
    'amount must be of type integer',
    'amount cannot be less than 100 XAF',
]

# Check if API key is configured
if not API_KEY:
    logger.warning("⚠️ FAPSHI_API_KEY is not configured! Set FAPSHI_API_KEY environment variable or payment will fail.")
    logger.warning("   To fix: Set environment variable 'FAPSHI_API_KEY' with your Fapshi API key")

def is_api_configured():
    """Check if the Fapshi API is properly configured"""
    return bool(API_KEY and API_USER)

def initiate_pay(data: dict):
    '''
        This function returns a dictionary with a link were a user is to be redirected in order to complete his payment

        required *

        data = {
            "amount": Integer *,
            "email": String,
            "userId": String,
            "externalId": String,
            "redirectUrl": String,
            "message": String
        }
    '''
    # Check if API is configured
    if not is_api_configured():
        logger.error("Payment failed: Fapshi API key not configured")
        return {
            'statusCode': 503, 
            'message': 'Payment service not configured. Please contact support.',
            'error': 'PAYMENT_SERVICE_UNAVAILABLE'
        }
    
    if(type(data) is not dict):
        return {'statusCode':400, 'message':ERRORS[1]}

    key = 'amount'
    if(key not in data):
        return {'statusCode':400, 'message':ERRORS[2]}

    if(type(data['amount']) is not int):
        return {'statusCode':400, 'message':ERRORS[3]}

    if(data['amount']<100):
        return {'statusCode':400, 'message':ERRORS[4]}

    url = BASE_URL+'/initiate-pay'
    try:
        r = requests.post(url=url, json=data, headers=HEADERS)
        resp = r.json()
        resp['statusCode'] = r.status_code
        return resp
    except Exception as e:
        return {'statusCode': 500, 'message': str(e)}

def payment_status(trans_id: str):
    '''
        This function returns a dictionary containing the details of the transaction with associated with the Id passed as parameter
    '''
    if(type(trans_id) is not str) or (not trans_id):
        return {'statusCode':400, 'message':ERRORS[0]}

    if(not re.search('^[a-zA-Z0-9]{8,10}$',trans_id)):
        return {'statusCode':400, 'message':'invalid transaction id'}

    url = BASE_URL+'/payment-status/'+trans_id
    try:
        r = requests.get(url=url, headers=HEADERS)
        resp = r.json()
        resp['statusCode'] = r.status_code
        return resp
    except Exception as e:
        return {'statusCode': 500, 'message': str(e)}

def expire_pay(trans_id: str):
    '''
        This function expires the transaction associated with the Id passed as parameter and returns a dictionary containing the details of the transaction
    '''
    if(type(trans_id) is not str) or (not trans_id):
        return {'statusCode':400, 'message':ERRORS[0]}

    if(not re.search('^[a-zA-Z0-9]{8,10}$',trans_id)):
        return {'statusCode':400, 'message':'invalid transaction id'}

    data = {"transId":trans_id}
    url = BASE_URL+'/expire-pay'
    try:
        r = requests.post(url=url, json=data, headers=HEADERS)
        resp = r.json()
        resp['statusCode'] = r.status_code
        return resp
    except Exception as e:
        return {'statusCode': 500, 'message': str(e)}
