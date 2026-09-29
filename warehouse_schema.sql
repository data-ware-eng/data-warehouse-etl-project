CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    title VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC
);

CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    product_id INT REFERENCES dim_products(product_id),
    user_id INT REFERENCES dim_users(user_id),
    quantity INT,
    total_amount NUMERIC
);
