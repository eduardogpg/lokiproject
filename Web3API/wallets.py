import json

from . import web3

def balance(wallet_address, token_address, token_abi):
    try:
        contract = web3.eth.contract(address=web3.toChecksumAddress(token_address), abi=json.loads(token_abi))

        address = web3.toChecksumAddress(web3.toChecksumAddress(wallet_address))
        balance = contract.functions.balanceOf(address).call()

        return web3.fromWei(balance, "ether")
    
    # https://paohuee.medium.com/interact-binance-smart-chain-using-python-4f8d745fe7b7
    except Exception as err:
        print(err)

        return None
