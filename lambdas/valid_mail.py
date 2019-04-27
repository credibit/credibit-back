import requests

def valid_mail(mail):
    url = 'https://pointsdb-trumail-v1.p.rapidapi.com/validate?email={}'.format(mail)
    headers = {
        "X-RapidAPI-Host": "pointsdb-trumail-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "f14cd51d87msh19885c10365d9f2p109e41jsn49e62da44290"
    }

    r = requests.get(url, headers=headers)

    validated = r.json()

    return validated['valid']
