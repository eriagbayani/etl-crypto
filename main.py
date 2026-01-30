from extract.api_client import get_crypto
from transform.clean_data import transform_crypto
from load.save_data_csv import save_crypto
# save to db
from load.save_data_db import load_data_to_db
import config

def run_etl():
    # extract
    raw_data = get_crypto()
    # Transform 
    df = transform_crypto(raw_data)

    # Load csv
    # save_crypto(df)
    # load to db (sqlite)
    load_data_to_db(df, config.DB_NAME, config.CRYPTO_TABLE)
    print("ETL completed!")

if __name__ == "__main__":
    run_etl()
