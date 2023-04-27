import requests

def fetch_data_from_api():
    url = " http://127.0.0.1:8000/admin"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
