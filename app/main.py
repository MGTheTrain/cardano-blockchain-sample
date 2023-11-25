from cardano_tools import CardanoWallet

# Initialize the Cardano wallet
wallet = CardanoWallet(
    base_url="http://localhost:8090/v2"  # URL of the cardano-wallet server
)

# Example: Get network information
network_info = wallet.get_network_information()
print(network_info)

# # Example: Create a new wallet
# wallet_name = "my_wallet"
# mnemonic = "your space-separated mnemonic words"
# wallet.create_wallet(wallet_name, mnemonic)