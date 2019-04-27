import requests

def check_site(url, company):
    try:
        r = requests.get(url)
        page = r.text

        return company.lower() in page.lower()
    except:
        return False
