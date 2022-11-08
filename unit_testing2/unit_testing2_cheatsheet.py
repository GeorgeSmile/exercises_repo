def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.com/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def get_country_code(key):