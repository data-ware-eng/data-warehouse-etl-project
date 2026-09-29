import pandas as pd
import psycopg2

# Load transformed data
dim_products = pd.read_csv("data/dim_products.csv")
dim_users = pd.read_csv("data/dim_users.csv")
fact_sales = pd.read_csv("data/fact_sales.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="etl_project",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into tables
for _, row in dim_products.iterrows():
    cur.execute(
        "INSERT INTO dim_products (product_id, title, category, price) VALUES (%s, %s, %s, %s)",
        (row["product_id"], row["title"], row["category"], row["price"])
    )

for _, row in dim_users.iterrows():
    cur.execute(
        "INSERT INTO dim_users (user_id, name, email) VALUES (%s, %s, %s)",
        (row["user_id"], row["name"], row["email"])
    )

for _, row in fact_sales.iterrows():
    cur.execute(
        "INSERT INTO fact_sales (sale_id, product_id, user_id, quantity, total_amount) VALUES (%s, %s, %s, %s, %s)",
        (row["sale_id"], row["product_id"], row["user_id"], row["quantity"], row["total_amount"])
    )

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL successfully.")
