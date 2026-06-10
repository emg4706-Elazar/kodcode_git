import requests



def safe_get(url):
    response1 = requests.get(url)
    if response1.status_code == 200:
        return response1.json()
    if response1.status_code == 404:
        return None
    else:
        raise Exception(response1.status_code)







