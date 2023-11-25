import argparse
from cardano.wallet import WalletService
from cardano.wallet import Wallet
from cardano.backends.walletrest import WalletREST

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a Cardano wallet and check balance.")
    parser.add_argument("--host", type=str, default="localhost", help="Wallet server host (default: localhost)")
    parser.add_argument("--port", type=int, default=8090, help="Wallet server port (default: 8090)")
    return parser.parse_args()

def create_wallet(ws: WalletService, wallet_name: str, wallet_mnemonic: str, passphrase: str) -> str:
    """
    Create a new wallet and return its ID.
    """
    wallet_id = ws.create_wallet(
        name=wallet_name,
        mnemonic=wallet_mnemonic,
        passphrase=passphrase,
    )
    return wallet_id

def get_wallet_by_id(wallet_id: str) -> Wallet:
    """
    Retrieve a wallet by its ID and return a Wallet object.
    """
    wal = Wallet(wallet_id, backend=WalletREST(port=8090))
    return wal

def delete_wallet_by_id(wal: Wallet) -> None:
    """
    Delete the specified wallet.
    """
    wal.delete()

def main() -> None:
    args = parse_args()

    # Initialize the WalletService with provided host and port
    ws = WalletService(WalletREST(host=args.host, port=args.port))

    wallet_id = create_wallet(
        ws,
        wallet_name="Test wallet",
        wallet_mnemonic="resist render west spin antique wild gossip thing syrup network risk gospel seek drop receive",
        passphrase="passphrase1234",
    )
    wal = get_wallet_by_id(wallet_id)
    delete_wallet_by_id(wal)

    # # Check wallet sync progress
    # wal.sync_progress()

    # # Get wallet balance
    # balance = wal.balance()
    # print(f"Wallet balance: {balance} ADA")

if __name__ == "__main__":
    main()
