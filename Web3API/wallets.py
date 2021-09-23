import json

from . import web3

def balance(wallet, token):
    contract = web3.eth.contract(address=token.address, abi=json.loads(token.abi))

    balance = contract.functions.balanceOf(wallet.address).call()
    return web3.fromWei(balance, "ether")
