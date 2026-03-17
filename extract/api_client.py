"""Extract cryptocurrency market data from CoinGecko API."""

import requests
import pandas as pd
from utils.logger import get_logger
logger = get_logger(__name__)

def get_crypto():
    """Fetch cryptocurrency market data from CoinGecko API in USD."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd"
    }

    response = requests.get(url, params=params, timeout=(3.05, 10))
    if response.status_code != 200:
        logger.error("API request failed with status %s",response.status_code )
    data = response.json()
    df = pd.DataFrame(data)
    return df

    #return response.json()  # <-- raw JSON, no transformation
