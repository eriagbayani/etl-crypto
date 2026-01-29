"""Save cryptocurrency data to CSV file."""

import pandas as pd


def save_crypto(df, filename='crypto.csv'):
    """
    Save a DataFrame to a CSV file.

    Args:
        df: pandas DataFrame to save
        filename: output CSV file path (default: 'crypto.csv')
    """
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} rows to {filename}")
