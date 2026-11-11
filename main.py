"""
main.py
-------
Runs the full Extract -> Transform -> Load pipeline.

Usage:
    python main.py
"""

from load import load
from transform import transform


def run_pipeline():
    print("=" * 50)
    print("AMAZON SALES ETL PIPELINE")
    print("=" * 50)

    customers, products, salespeople, orders = transform()  # transform() calls extract()
    load(customers, products, salespeople, orders)

    print("=" * 50)
    print("ETL pipeline completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()
