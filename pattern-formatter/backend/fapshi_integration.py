import re
import requests
import os

# Configuration - Production Mode
# API credentials should be set via environment variables
BASE_URL = 'https://live.fapshi.com'
API_USER = os.environ.get('FAPSHI_API_USER', 'c02a978a-5e79-4b8e-9906-32847acaacc5')
API_KEY = os.environ.get('FAPSHI_API_KEY', '')

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
