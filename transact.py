import json
import web3
from web3 import Web3, utils

# Connecting to the network through MetaMask's local RPC server
rpc_url = 'https://polygon-mumbai.infura.io/v3/'  # Infura RPC URL
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Checks if the connection is successful
if w3.is_connected():
    print("Connected to the network")
else:
    print("Failed to connect to the network")
    exit(1)

# Enter your token's ABI
abi = ''

# Enter your token's contract address
address = ""

# Creates a contract instance
contract = w3.eth.contract(address=address, abi=json.loads(abi))

# Displays the total supply of the token in ether
totalSupply = contract.functions.totalSupply().call()
print(w3.from_wei(totalSupply, 'ether'))
# print(contract.functions.owner().call())

# Sends a transaction

# Addresses needed

# Your metamask wallet's private key
private_key = ''

# Transaction Sender and Recipient Addresses
sender_address = ''
recipient_address = ''

# Transaction amount
amount = w3.to_wei('999.99', "ether")

# Adding a transaction tax margin
margin = 1.5  # Adjustable

# Transaction build

# Update the chain's variables according to the blockchain you're using
transaction = contract.functions.transfer(recipient_address, amount).build_transaction({
    'chainId': 80001,
    'gas': 4000000,
    'gasPrice': w3.to_wei('5', 'gwei'),
    'nonce': w3.eth.get_transaction_count(w3.to_checksum_address(sender_address)),
})

# Signing the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

# Sending the transaction

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Printing the transaction's details
print('Transaction Hash: ', tx_hash.hex())
print("Transaction Details:")
print("From:", sender_address)
print("To:", recipient_address)
print("Amount:", amount)
print("Gas Price:", w3.to_wei('0.0005', 'ether'))  # Adjust gas price as needed
print("Gas Limit:", 200000)  # Adjust gas limit as needed
print("Nonce:", w3.eth.get_transaction_count(w3.to_checksum_address(sender_address)))
