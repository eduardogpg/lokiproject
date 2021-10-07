import requests

def get_prices(ids):
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd')

    if response.status_code == 200:
        return response.json()

    return dict()