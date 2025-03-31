## **✨ Features**
- ✅ Compatible with any ERC-20 token
- 🔄 Fetches on-chain data from your blockchain RPC
- 🔓 No authentication required
- 📊 CoinGecko-compliant endpoints:
- /api/total-supply
- /api/circulating-supply
- /api/full-supply (optional extended JSON)


## **⚙️ Requirements**
- Python 3.9 or higher
- A server with internet access (e.g., DigitalOcean, AWS, etc.)
- Your token’s contract address
- ABI (Application Binary Interface) file
- A list of excluded wallets (locked, team, burn, etc.)


## **📁 File Structure**
```
token_supply_api/
├── token_supply_api.py      # Main Flask app
├── token_abi.json           # Your token ABI (ERC-20 standard or custom)
├── .env                     # Token config (RPC URL, excluded wallets, etc.)
└── README.md                # This file
```


## **✏️ Setup Instructions**

**1. Clone this Repo**
```bash
git clone https://github.com/yourname/token_supply_api.git
cd token_supply_api
```

**2. Create a Python Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install flask web3 python-dotenv
```

**4. Create .env File**
```bash
cp .env.example .env
```


**5. Edit the .env file:**
```bash
CONTRACT_ADDRESS=0xYourTokenAddressHere
EXCLUDED_WALLETS=0xMarketingWallet,0xBurnWallet
DECIMALS=18
RPC_URL=https://api.avax.network/ext/bc/C/rpc
```

**6. Add Your Token ABI**
- Save the ABI as a JSON string in token_abi.json
- You can get it from SnowTrace, Etherscan, or your developer

**7. Run the Server**
```bash
python token_supply_api.py
```

**8. Visit:**
```bash
http://your-server-ip:5050/api/total-supply
http://your-server-ip:5050/api/circulating-supply
```


## **🌐 Deploying to a Server (e.g. DigitalOcean)**

*- Assuming Ubuntu server:*

**A. Connect via SSH**
```bash
ssh root@your.server.ip
```
**B. Install Python, pip, git**
```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git
```
**C. Clone and Set Up**
```bash
git clone https://github.com/yourname/token_supply_api.git
cd token_supply_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or manually install packages
```
**D. (Optional) Run as a background service**

*- Use tmux, screen, or create a systemd service to run it in the background.*

**E. (Optional) Open port 5050 in firewall**

*- If using UFW:*
```bash
sudo ufw allow 5050
```


## **🤔 Example API Output**
```bash
/api/circulating-supply
{
  "circulating_supply": "58861548280198.937500000000000000"
}
```
```bash
/api/total-supply

{
  "total_supply": "69420000000000.000000000000000000"
}
```
```bash
/api/full-supply

{
  "total_supply": "69420000000000.000000000000000000",
  "excluded_wallets": {
    "0xMarketing": 4789980000000.0,
    "0xBurn": 5768471719801.06
  },
  "circulating_supply": "58861548280198.937500000000000000"
}
```


## **🌟 License**

**MIT**

*For questions or help, reach out at [0xODanny@gmail.com] or open an issue in this repo.*

