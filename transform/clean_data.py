"""Transform and clean cryptocurrency market data."""

import pandas as pd


def transform_crypto(raw_data):
    """
    Transform raw cryptocurrency data into a clean DataFrame.

    Args:
        raw_data: raw JSON data from CoinGecko API

    Returns:
        DataFrame with columns: Name, Symbol, PriceUSD, MarketCap, Rank
        sorted by market cap in descending order
    """
    df = pd.DataFrame(raw_data)

    df = df[["name", "symbol", "current_price", "market_cap"]]

    df = df.rename(columns={
        "name": "Name",
        "symbol": "Symbol",
        "current_price": "PriceUSD",
        "market_cap": "MarketCap"
    })

    df = df.sort_values("MarketCap", ascending=False).reset_index(drop=True)

    df["Rank"] = df.index + 1

    return df