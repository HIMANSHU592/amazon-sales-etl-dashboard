"""
load.py
-------
Load step of the ETL pipeline: writes the cleaned tables into MySQL using SQLAlchemy.

Database credentials are read from environment variables (see .env.example),
so no password is stored in the code.
"""

import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "amazon_sales")


def get_engine():
    url = f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(url)


def load(customers, products, salespeople, orders):
    engine = get_engine()
    # if_exists="replace" rebuilds each table on every run (fine for this project).
    customers.to_sql("customers", engine, if_exists="replace", index=False)
    products.to_sql("products", engine, if_exists="replace", index=False)
    salespeople.to_sql("salespeople", engine, if_exists="replace", index=False)
    orders.to_sql("orders", engine, if_exists="replace", index=False)


if __name__ == "__main__":
    from transform import transform

    load(*transform())
    print("Data loaded successfully!")
