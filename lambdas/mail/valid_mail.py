import requests
import json

def valid_mail(event, context):
    file = event['body']
    dic = json.loads(file)

    mail = dic['mail']

    url = 'https://pointsdb-trumail-v1.p.rapidapi.com/validate?email={}'.format(mail)
    headers = {
        "X-RapidAPI-Host": "pointsdb-trumail-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "f14cd51d87msh19885c10365d9f2p109e41jsn49e62da44290"
    }

    r = requests.get(url, headers=headers)

    validated = r.json()

    if validated['valid']:
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'text/plain' },
            'body': 'Email valid'
        }
    return {
        'statusCode': 400,
        'headers': { 'Content-Type': 'text/plain' },
        'body': 'Email not valid'
    }
