from web3 import Web3

# Connect to the Ethereum network (using Infura here)
infra_api_key = "2d485d8257c4404394a021e9613f52e9"
infura_url = f"https://mainnet.infura.io/v3/{infra_api_key}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Ensure your Web3 instance is connected
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect")

# Your account details
private_key = "6c9cd41d5ea7fbe5b4c9058fc2b70dc95d54d0654437411041495cf950c2fed7"
account = web3.eth.account.from_key(private_key)
print(f"Account address: {account.address}")

# Check balance
balance = web3.eth.get_balance(account.address)
print(f"Balance: {web3.from_wei(balance, 'ether')} Ether")
