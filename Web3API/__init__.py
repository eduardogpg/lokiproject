from web3 import Web3
from web3.middleware import geth_poa_middleware

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

