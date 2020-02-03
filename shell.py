
import json , os , hashlib 
from web3 import Web3, HTTPProvider
#Importe les adresses et les clès
def import_log():
    with open('log_id.json') as json_data:
        data_dict = json.load(json_data)
        return data_dict

#Initialisation du Web3 provider
ganache_url = "http://127.0.0.1:7545"
w3 = Web3( Web3.HTTPProvider(ganache_url) )
os.system("clear")

#On set le default account sur l'adresse du locataire 
w3.eth.defaultAccount = import_log()['adresseLocataire']

print("Connection au serveur : " + str(w3.isConnected()))
print(" ")

contract_abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"amount","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAmount","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getLocataire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getProprietaire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"hashDoc","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_proprietaire","type":"address"},{"internalType":"bytes32","name":"_hashDoc","type":"bytes32"},{"internalType":"uint24","name":"_amount","type":"uint24"}],"name":"initializationContract","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"_hashDoc","type":"bytes32"},{"internalType":"uint24","name":"_amount","type":"uint24"}],"name":"launchContract","outputs":[{"internalType":"bool","name":"check","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"locataire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"proprietaire","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"validationLocataire","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]')
contract_adress = w3.toChecksumAddress("0x3C661242777e89553F0728E8fef879a9c1C924ec")

contract = w3.eth.contract(address = contract_adress , abi = contract_abi)

_hash = hashlib.sha256(bytes(32000)).digest()

valid = contract.functions.initializationContract(import_log()['adresseProprietaire'],_hash, 3000).transact()
print()
print(" ")
print(contract.functions.getLocataire().call())
print(contract.functions.getProprietaire().call())
print(contract.functions.getAmount().call())