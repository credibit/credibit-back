import requests
import json

def check_site(event, context):
    file=event['body']
    dic = json.loads(file)

    url = dic['url']
    company = dic['company']

    try:
        r = requests.get(url)
        page = r.text

        valid_company = company.lower() in page.lower()

        if valid_company:
            return {
                'statusCode': 200,
                'headers': { 'Content-Type': 'text/plain' },
                'body': 'Company exists'
            }
        else:
            return {
                'statusCode': 404,
                'headers': { 'Content-Type': 'text/plain' },
                'body': 'Company does not exist'
            }
    except:
        return {
            'statusCode': 404,
            'headers': { 'Content-Type': 'text/plain' },
            'body': 'Company does not exist'
        }
