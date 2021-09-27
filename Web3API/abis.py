import json
import requests

from . import web3

URL_BSC = "https://api.bscscan.com/api"

def abi(token_address):
    contract_address = web3.toChecksumAddress(str(token_address))
    API_ENDPOINT = URL_BSC + "?module=contract&action=getabi&address=" + contract_address

    response = requests.get(url = API_ENDPOINT)
    if response.status_code == 200 and response.json()['status'] == "1":
        return response.json()["result"]

    return None