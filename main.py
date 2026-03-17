"""Main ETL orchestration script for cryptocurrency data pipeline."""

import os

import requests
from dotenv import load_dotenv

from extract.api_client import get_crypto
from transform.clean_data import transform_crypto
from load.save_data_csv import save_crypto
from load.save_data_db import load_data_to_db
import config
from utils.logger import get_logger

logger = get_logger(__name__)

# Load environment variables from .env file
load_dotenv()

def trigger_n8n(df, limit=10):
    """
    Send transformed crypto data to n8n webhook

    Args:
        df: DataFrame with crypto data
        limit: Number of top cryptos to send (default: 10)
    """
    webhook_url = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5680/webhook-test/crypto-report")

    # Get only top N cryptos
    top_cryptos = df.head(limit)
    payload = top_cryptos.to_dict(orient="records")  # convert DataFrame to JSON

    try:
        response = requests.post(webhook_url, json=payload, timeout=30)
        if response.status_code == 200:
            logger.info("n8n webhook triggered successfully! Sent top %s cryptos.", limit)
        else:
            logger.error("Webhook failed: %s %s", response.status_code, response.text)
    except Exception as e:
        logger.error("Error triggering webhook: %s", e)

def run_etl():
    """
    Run the complete ETL pipeline.

    Extracts cryptocurrency data from CoinGecko API,
    transforms it into a clean DataFrame,
    and loads it to CSV and Google Sheets via n8n webhook.
    """
    # extract
    raw_data = get_crypto()
    # Transform
    df = transform_crypto(raw_data)

    # Load to CSV
    save_crypto(df)

    # Trigger n8n webhook to write to Google Sheets
    trigger_n8n(df)
    # Optional: Also load to db (sqlite)
    # load_data_to_db(df, config.DB_PATH, config.CRYPTO_TABLE)

    logger.info("ETL completed!")

if __name__ == "__main__":
    run_etl()
