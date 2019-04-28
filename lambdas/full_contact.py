import requests
import json

def getFullContact(domain):
    headers = {
        "X-RapidAPI-Host": "fullcontact-enrich-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "f14cd51d87msh19885c10365d9f2p109e41jsn49e62da44290",
        "Content-Type": "application/json"
    }
    params = {
        'domain': domain
    }

    r = requests.post("https://fullcontact-enrich-v1.p.rapidapi.com/company.enrich", headers=headers, data=json.dumps(params))

    company_data = r.json()

    return_data = {}

    return_data['name'] = company_data['name']
    return_data['twitter'] = company_data['twitter']
    return_data['linkedin'] = company_data['linkedin']
    return_data['facebook'] = company_data['facebook']
    return_data['website'] = company_data['website']
    return_data['founded'] = company_data['founded']
    return_data['employees'] = company_data['employees']

    return return_data
