import requests

def getLanguages(url):
    response=requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching languages")
        return None
