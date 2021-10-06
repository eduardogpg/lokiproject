import json
from . import web3

def total_balance_of(token, wallet):

    contract = web3.eth.contract(
        address=web3.toChecksumAddress(token.address),
        abi=json.loads(token.abi)
    )
    
    balance = contract.functions.balanceOf(web3.toChecksumAddress(wallet.address)).call()
    print(balance)
    print(balance)
    print(balance)
    print(wallet.address)

    return balance