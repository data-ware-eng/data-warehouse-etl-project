CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
	title VARCHAR(255),
	category VARCHAR(255),
	price DECIMAL(10,2)
);

CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,
	username VARCHAR(255),
	email VARCHAR(255)
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
	product_id INT,
	user_id INT,
	quan
