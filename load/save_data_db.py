import pandas as pd
import sqlite3


def load_data_to_db(df, db_path, table_name):
    """
    Load a DataFrame into a SQLite database table.

    Args:
        df: pandas DataFrame to load
        db_path: path to SQLite database file
        table_name: name of the table to create/replace
    """
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)