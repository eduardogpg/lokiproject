import json

from . import web3

def total_balance_of(token, wallet):
    try:
        contract_address = web3.toChecksumAddress(str(token.address))
        contract = web3.eth.contract(address=contract_address, abi=token.abi)

        address = web3.toChecksumAddress(wallet.address)
        balance = contract.functions.balanceOf(address).call()
        print(balance)
        print(balance)
        print(type(balance))
        


        # return  web3.fromWei(web3.eth.getBalance(address),'ether')
        return balance

        # return web3.fromWei(balance, "ether")
    
    except Exception as err:
        print(">>>>> ERROR: ")
        print(err)

        return -100