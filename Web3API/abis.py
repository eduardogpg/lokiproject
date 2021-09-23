import json
import requests

from . import web3

URL_BSC = "https://api.bscscan.com/api"

def abi(token):
    API_ENDPOINT = URL_BSC + "?module=contract&action=getabi&address=" + str(token.address)
    
    response = requests.get(url = API_ENDPOINT)
    if response.status_code == 200:
        return response.json()["result"]
