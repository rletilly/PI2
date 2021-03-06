
import json , os , hashlib 
from web3 import Web3, HTTPProvider
os.system("clear")
#Importe les adresses et les clès
def import_log():
    with open('log_id.json') as json_data:
        data_dict = json.load(json_data)
        return data_dict

#Initialisation du Web3 provider
ganache_url = "http://127.0.0.1:7545"
w3 = Web3( Web3.HTTPProvider(ganache_url) )

#On set le default account sur l'adresse du locataire 
w3.eth.defaultAccount = import_log()['adresseLocataire']
locataire = import_log()['adresseLocataire']

print("Connection au serveur : " + str(w3.isConnected()))
print(" ")

contract_abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"amount","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAmount","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getLocataire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getProprietaire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"goCompound","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"hashDoc","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_proprietaire","type":"address"},{"internalType":"bytes32","name":"_hashDoc","type":"bytes32"},{"internalType":"uint24","name":"_amount","type":"uint24"}],"name":"initializationContract","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"_hashDoc","type":"bytes32"},{"internalType":"uint24","name":"_amount","type":"uint24"}],"name":"launchContract","outputs":[{"internalType":"bool","name":"check","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"locataire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"proprietaire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"validationLocataire","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]')
contract_adress = w3.toChecksumAddress("0x657272559E1F06BA0338B63B59750E9a21288cB7")






#web3.eth.sendTransaction({from:web3.eth.accounts[0],to:"0x943",value:  "1000000000000000000", data: "0xdf"}
contract = w3.eth.contract(address = contract_adress , abi = contract_abi)

_hash = hashlib.sha256(bytes(32000)).digest()

txn = contract.functions.initializationContract(import_log()['adresseProprietaire'],_hash, 0000).buildTransaction({
      'chainId': 13999911119,
      'gas': 70000,
      'value': 10000000000000000000,
      'gasPrice': w3.toWei('8', 'gwei'),
      'nonce': w3.eth.getTransactionCount(locataire)
    })
signed_txn = w3.eth.account.sign_transaction(txn, private_key=import_log()['privateKeyLocataire'])
#w3.eth.sendRawTransaction(signed_txn.rawTransaction)
contract.functions.goCompound().transact()


print(txn)
print(" ")
print(contract.functions.getLocataire().call())
print(contract.functions.getProprietaire().call())
print(contract.functions.getBalance().call())