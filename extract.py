import requests
import pandas as pd

# Extract products from Fake Store API
products_url = "https://fakestoreapi.com/products"
products = requests.get(products_url).json()
df_products = pd.DataFrame(products)
df_products.to_csv("data/products.csv", index=False)

# Extract users from Fake Store API
users_url = "https://fakestoreapi.com/users"
users = requests.get(users_url).json()
df_users = pd.DataFrame(users)
df_users.to_csv("data/users.csv", index=False)

print("Data extracted and saved to CSV files.")
