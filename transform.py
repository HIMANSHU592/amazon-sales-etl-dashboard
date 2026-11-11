import pandas as pd
from extract import extract


def transform():
    df = extract()

    # Creating customer table
    customers = df[['Customer ID', 'Customer Name']]
    customers = customers.drop_duplicates(subset='Customer ID')

    # Creating products table
    products = df[['Product Name', 'Product Category']].copy()

    # Find duplicates
    products_duplicates = products[products.duplicated()]

    # Remove duplicates
    products = products.drop_duplicates().copy()

    # Add new column product_id
    products['product_id'] = range(1, len(products) + 1)

    # Create dictionary to search product_id using product name and category
    product_lookup = products.set_index(
        ['Product Name', 'Product Category']
    )['product_id'].to_dict()

    # Add product_id into original df
    df['product_id'] = df.apply(
        lambda r: product_lookup[
            (r['Product Name'], r['Product Category'])
        ],
        axis=1
    )

    # Creating salesperson table
    salespeople = df[['Salesperson']].copy()

    # Check duplicates
    salespeople_duplicate = salespeople[salespeople.duplicated()]

    # Remove duplicates
    salespeople = salespeople.drop_duplicates().copy()

    # Add new column salesperson_id
    salespeople['salesperson_id'] = range(1, len(salespeople) + 1)

    # Dictionary to search salesperson_id using name
    salesperson_lookup = salespeople.set_index(
        'Salesperson'
    )['salesperson_id'].to_dict()

    # Add salesperson_id into df
    df['salesperson_id'] = df.apply(
        lambda r: salesperson_lookup[r['Salesperson']],
        axis=1
    )

    # Creating orders table
    orders = df[
        [
            'Order ID',
            'Order Date',
            'Customer ID',
            'product_id',
            'salesperson_id',
            'Region',
            'Quantity Sold',
            'Unit Price',
            'Discount (%)',
            'Payment Method',
            'Order Status',
            'Total Sales',
            'Profit Margin'
        ]
    ]

    # Rename customer columns
    customers = customers.rename(columns={
        'Customer ID': 'customer_id',
        'Customer Name': 'customer_name'
    })

    # Rename product columns
    products = products.rename(columns={
        'Product Name': 'product_name',
        'Product Category': 'category'
    })

    # Rename salesperson columns
    salespeople = salespeople.rename(columns={
        'Salesperson': 'salesperson_name'
    })

    # Rename order columns
    orders = orders.rename(columns={
        'Order ID': 'order_id',
        'Order Date': 'order_date',
        'Customer ID': 'customer_id',
        'Region': 'region',
        'Quantity Sold': 'quantity_sold',
        'Unit Price': 'unit_price',
        'Discount (%)': 'discount_pct',
        'Payment Method': 'payment_method',
        'Order Status': 'order_status',
        'Total Sales': 'total_sales',
        'Profit Margin': 'profit_margin'
    })

    # Make sure order_date is a proper date
    # dayfirst=True because dates are in DD-MM-YYYY format (e.g. "13-01-2019")
    orders['order_date'] = pd.to_datetime(orders['order_date'], dayfirst=True)

    return customers, products, salespeople, orders


if __name__ == "__main__":
    # Test this file on its own: python transform.py
    customers, products, salespeople, orders = transform()

    print(customers)
    print(products)
    print(salespeople)
    print(orders) 