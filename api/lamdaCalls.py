import requests
import json

def getCredit(params):
    desired_months = params['plazoDeseado']

    results = {
        'A': {
            'months': [3, 6, 12, desired_months]
        },
        'B': {
            'months': [12, desired_months if desired_months <= 36 else 36]
        },
        'C': {
            'months': [12, 24]
        }
    }

    lambda_api = 'https://tlnlicdqk0.execute-api.us-east-2.amazonaws.com/prod/paymentCapacity'
    r = requests.post(lambda_api, data=json.dumps(params))
    
    credit = r.json()
    body = json.loads(credit['body'])
    response = body['response']

    category = response[0]

    if category == 'D':
        return False
    
    result = results[category]
    result['ammount'] = response[1]

    return result
