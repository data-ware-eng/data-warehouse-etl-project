import pandas as pd

# Load extracted data
df_products = pd.read_csv("data/products.csv")
df_users = pd.read_csv("data/users.csv")

# Clean products data
df_products["title"] = df_products["title"].str.strip()
df_products["price"] = df_products["price"].astype(float)

# Clean users data


# Create dimension tables
dim_products = df_products[["id", "title", "category", "price"]].rename(columns={"id": "product_id"})
dim_users = df_users.rename(columns={"id": "user_id"})

# Example fact table (sales simulation)
fact_sales = pd.DataFrame({
    "sale_id": range(1, 6),
    "product_id": [1, 2, 3, 4, 5],
    "user_id": [1, 2, 3, 1, 2],
    "quantity": [2, 1, 4, 1, 3],
    "total_amount": [40.0, 20.0, 120.0, 15.0, 75.0]
})

# Save transformed data
dim_products.to_csv("data/dim_products.csv", index=False)
dim_users.to_csv("data/dim_users.csv", index=False)
fact_sales.to_csv("data/fact_sales.csv", index=False)

print("Data transformed and saved as dimension and fact tables.")
