Token Supply API - Standalone Flask App

A simple, public-facing REST API to expose your token's total supply, circulating supply, and optionally full wallet breakdowns — ideal for CoinGecko or CoinMarketCap listing submissions.

✨ Features

Compatible with any ERC-20 token

Fetches on-chain data from your blockchain RPC

No authentication required

CoinGecko-compliant endpoints:

/api/total-supply

/api/circulating-supply

/api/full-supply (optional extended JSON)

⚡ Requirements

Python 3.9 or higher

A server with internet access (e.g., DigitalOcean Droplet)

Your token's contract address

ABI (Application Binary Interface) file

A list of excluded wallets (locked, team, burn, etc.)

📁 File Structure

token_supply_api/
├── token_supply_api.py      # Main Flask app
├── token_abi.json           # Your token ABI (ERC-20 standard or custom)
├── .env                     # Token config (RPC URL, excluded wallets, etc.)
└── README.md                # This file

✏️ Setup Instructions

1. Clone this Repo

git clone https://github.com/yourname/token_supply_api.git
cd token_supply_api

2. Create a Python Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install flask web3 python-dotenv

4. Create .env File

cp .env.example .env

Edit the .env file:

CONTRACT_ADDRESS=0xYourTokenAddressHere
EXCLUDED_WALLETS=0xMarketingWallet,0xBurnWallet
DECIMALS=18
RPC_URL=https://api.avax.network/ext/bc/C/rpc

5. Add Your Token ABI

Save the ABI as a JSON string in token_abi.json

You can get it from SnowTrace, Etherscan, or your developer

6. Run the Server

python token_supply_api.py

Visit:

http://your-server-ip:5050/api/total-supply

http://your-server-ip:5050/api/circulating-supply

🌐 Deploying to a Server (e.g. DigitalOcean)

Assuming Ubuntu server:

A. Connect via SSH

ssh root@your.server.ip

B. Install Python, pip, git

sudo apt update && sudo apt install -y python3 python3-pip python3-venv git

C. Clone and Set Up

git clone https://github.com/yourname/token_supply_api.git
cd token_supply_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or manually install packages

D. (Optional) Run as a background service

Use tmux, screen, or create a systemd service to run it in the background.

E. (Optional) Open port 5050 in firewall

If using UFW:

sudo ufw allow 5050

🤔 Example API Output

/api/circulating-supply

{
  "circulating_supply": "58861548280198.937500000000000000"
}

/api/total-supply

{
  "total_supply": "69420000000000.000000000000000000"
}

/api/full-supply

{
  "total_supply": "69420000000000.000000000000000000",
  "excluded_wallets": {
    "0xMarketing": 4789980000000.0,
    "0xBurn": 5768471719801.06
  },
  "circulating_supply": "58861548280198.937500000000000000"
}

🌟 License

MIT

For questions or help, reach out at [your_email@example.com] or open an issue in this repo.

