-- Reference design for the amazon_sales database. The pipeline (load.py) recreates tables via pandas to_sql.


CREATE DATABASE IF NOT EXISTS amazon_sales;
USE amazon_sales;


CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS salespeople (
    salesperson_id INT PRIMARY KEY,
    salesperson_name VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(50),
    product_id INT,
    salesperson_id INT,
    region VARCHAR(50),
    quantity_sold INT,
    unit_price DECIMAL(10,2),
    discount_pct DECIMAL(5,2),
    payment_method VARCHAR(30),
    order_status VARCHAR(20),
    total_sales DECIMAL(12,2),
    profit_margin DECIMAL(12,2),
    order_year INT,
    order_month INT,
    order_quarter INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (salesperson_id) REFERENCES salespeople(salesperson_id)
);
