import json
import requests

from . import web3

URL_BSC = "https://api.bscscan.com/api"

def abi(token):
    contract_address = web3.toChecksumAddress(str(token.address))
    API_ENDPOINT = URL_BSC + "?module=contract&action=getabi&address=" + contract_address

    response = requests.get(url = API_ENDPOINT)
    if response.status_code == 200 and response.json()['status'] == "1":
        return response.json()["result"]

    return None


def total_supply(token):
    try:
        contract_address = web3.toChecksumAddress(str(token.address))
        contract = web3.eth.contract(address=contract_address, abi=token.abi)

        supply = contract.functions.totalSupply().call()
        return web3.fromWei(supply, "ether")
    
    except Exception as err:
        print(err)

        return 0 # None is not a good idea
