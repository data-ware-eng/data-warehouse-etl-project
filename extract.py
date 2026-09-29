import requests
import pandas as pd

# Extract products from Fake Store API
products_url = "https://dummyjson.com/products"
respuesta_products = requests.get(products_url)
print(respuesta_products.status_code)
products = respuesta_products.json()["products"]
df_products = pd.DataFrame(products)
df_products.to_csv("data/products.csv", index=False)
users_url = "https://dummyjson.com/users"

# Extract users from Fake Store API
respuesta_usuarios = requests.get(users_url)
users = respuesta_usuarios.json()["users"]
df_users = pd.DataFrame(users)
df_users.to_csv("data/users.csv", index=False)

print("Data extracted and saved to CSV files.")
