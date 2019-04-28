import requests
import json

def getCredit(params):
    desired_months = params['plazoDeseado']

    results = {
        'A': {
            'months': [3, 6, 12, desired_months],
            'is_valid': True
        },
        'B': {
            'months': [12, desired_months if desired_months <= 36 else 36],
            'is_valid': True
        },
        'C': {
            'months': [12, 24],
            'is_valid': True
        }
    }

    lambda_api = 'https://tlnlicdqk0.execute-api.us-east-2.amazonaws.com/prod/paymentCapacity'
    r = requests.post(lambda_api, data=json.dumps(params))
    
    credit = r.json()
    body = json.loads(credit['body'])
    response = body['response']

    category = response[0]

    if category == 'D':
        return {
            'is_valid': False
        }
    
    result = results[category]
    result['ammount'] = response[1]

    return result

def verifySite(url, company):
    lambda_api = 'https://tlnlicdqk0.execute-api.us-east-2.amazonaws.com/prod/checkSiteAvailability'
    r = requests.post(lambda_api, data=json.dumps({ 'url': url, 'company': company }))

    return r.status_code == 200

def verifyEmail(email):
    lambda_api = 'https://tlnlicdqk0.execute-api.us-east-2.amazonaws.com/prod/validateMail'
    r = requests.post(lambda_api, data=json.dumps({ 'mail': email }))
    return r.status_code == 200
