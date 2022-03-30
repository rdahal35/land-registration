from web3 import Web3, contract
import json


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = '0xB7dbfc47109CC0529780AF0124ADD5C84d10535E'

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerSet","type":"event"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"changeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
bytecode = "608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167f342827c97908e5e2f71151c08502a66d44b6f758e3ac2f1de95f02eb95f0a73560405160405180910390a3610290806100db6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063893d20e81461003b578063a6f9dae11461006f575b600080fd5b6100436100b3565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6100b16004803603602081101561008557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506100dc565b005b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461019d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f43616c6c6572206973206e6f74206f776e65720000000000000000000000000081525060200191505060405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1660008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f342827c97908e5e2f71151c08502a66d44b6f758e3ac2f1de95f02eb95f0a73560405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505056fea2646970667358221220fad760a1b4ede4678d0696a51a4817b14e77b392c8ed0747a86407f71b8f4ab364736f6c63430007060033"
address = web3.toChecksumAddress('0xbdf5454E7F50C45a0758B6D7a94c02933BD5d6a6')

# contract = web3.eth.contract(address=address, abi=abi)
# accout = web3.eth.account.create()
def create_owner():
    Owner = web3.eth.contract(abi=abi, bytecode=bytecode)

    tx_hash = Owner.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    contract = web3.eth.contract(
        address= tx_receipt.contractAddress,
        abi= abi
    )

    print(contract.functions.getOwner().call())


# print(contract.functions.getOwner().call())

# tx_hash = contract.functions.changeOwner('0xb707c235b12331710A16d7Fdc96a037cC2773b9D').transact()

# print(tx_hash)

