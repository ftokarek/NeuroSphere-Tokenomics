import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "category": "pump-fun",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params).json()

data = []

for token in response:
    data.append({
        "name": token["name"],
        "symbol": token["symbol"],
        "price": token["current_price"],
        "market_cap": token["market_cap"],
        "circulating_supply": token["circulating_supply"],
        "total_supply": token.get("total_supply"),
        "volume_24h": token["total_volume"],
        "price_change_24h": token["price_change_percentage_24h"],
        "link": f"https://www.coingecko.com/en/coins/{token['id']}"
    })
    
df = pd.DataFrame(data)
df.to_csv("../../data/raw/pumpfun_top100.csv", index=False)
print(df.head())