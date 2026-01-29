import requests

def get_crypto():
    """Fetch cryptocurrency market data from CoinGecko API in USD."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd"
    }

    response = requests.get(url, params=params, timeout=(3.05, 10))
    if response.status_code != 200:
        print(f"API request failed with status {response.status_code}")
    
    return response.json()  # <-- raw JSON, no transformation
