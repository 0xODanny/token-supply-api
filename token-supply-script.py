from flask import Flask, jsonify
from web3 import Web3
import os

app = Flask(__name__)

# Set these before deploying
RPC_URL = os.getenv("RPC_URL", "https://api.avax.network/ext/bc/C/rpc")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # required
EXCLUDED_WALLETS = os.getenv("EXCLUDED_WALLETS", "").split(",")  # comma-separated
DECIMALS = int(os.getenv("DECIMALS", 18))

# Load ABI from file
with open("token_abi.json") as f:
    ABI = f.read()

web3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

def fetch_total_supply():
    return contract.functions.totalSupply().call() / 10**DECIMALS

def fetch_balance(addr):
    return contract.functions.balanceOf(Web3.to_checksum_address(addr)).call() / 10**DECIMALS

def fetch_circulating_supply():
    total = fetch_total_supply()
    excluded = sum(fetch_balance(w) for w in EXCLUDED_WALLETS if w)
    return total - excluded

@app.route("/api/total-supply")
def total_supply_endpoint():
    return jsonify({"total_supply": f"{fetch_total_supply():.18f}"})

@app.route("/api/circulating-supply")
def circulating_supply_endpoint():
    return jsonify({"circulating_supply": f"{fetch_circulating_supply():.18f}"})

@app.route("/api/full-supply")
def full_supply_endpoint():
    total = fetch_total_supply()
    excluded = {wallet: fetch_balance(wallet) for wallet in EXCLUDED_WALLETS if wallet}
    return jsonify({
        "total_supply": f"{total:.18f}",
        "excluded_wallets": excluded,
        "circulating_supply": f"{total - sum(excluded.values()):.18f}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)