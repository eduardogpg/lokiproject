import json
from . import web3

def total_balance_of(wallet, token):

    contract = web3.eth.contract(
        address=web3.toChecksumAddress(token.address),
        abi=json.loads(token.abi)
    )
    
    balance = contract.functions.balanceOf(web3.toChecksumAddress(wallet.address)).call()
    return balance