"""Save cryptocurrency data to CSV file."""
from utils.logger import get_logger
logger = get_logger(__name__)

"""Save cryptocurrency data to CSV file."""
def save_crypto(df, filename='crypto.csv'):
    """
    Save a DataFrame to a CSV file.

    Args:
        df: pandas DataFrame to save
        filename: output CSV file path (default: 'crypto.csv')
    """
    df.to_csv(filename, index=False)
    logger.info("Saved %s rows to %s", len(df), filename)
