"""
extract.py
----------
Extract step of the ETL pipeline: reads the raw Amazon sales CSV into a DataFrame.
"""

from pathlib import Path

import pandas as pd

# Path is relative to this file, so the project runs on any machine.
SOURCE_FILE = Path(__file__).parent / "data" / "amazon_sales_dataset_2019_2024_corrected.csv"


def extract() -> pd.DataFrame:
    return pd.read_csv(SOURCE_FILE)


if __name__ == "__main__":
    print(extract().head())
