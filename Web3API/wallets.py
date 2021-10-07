import json
from . import web3

def total_balance_of(token_address, token_abi, wallet_address):

    contract = web3.eth.contract(
        address=web3.toChecksumAddress(token_address),
        abi=json.loads(token_abi)
    )
    
    balance = contract.functions.balanceOf(web3.toChecksumAddress(wallet_address)).call()
    return balance