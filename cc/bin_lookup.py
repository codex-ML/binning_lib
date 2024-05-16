import requests

def bin_lookup(bin_digit):
    url = f"https://lookup.binlist.net/{bin_digit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"
