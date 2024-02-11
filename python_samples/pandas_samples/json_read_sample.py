import pandas as pd
import json

# Sample JSON data
json_data = '''
{
  "customer": {
    "name": "John Doe",
    "age": 35,
    "email": "john.doe@example.com",
    "address": {
      "city": "New York",
      "country": "USA",
      "zipcode": "10001"
    },
    "orders": [
      {
        "order_id": "123456",
        "products": [
          {
            "name": "Smartphone",
            "price": 799.99,
            "quantity": 1
          },
          {
            "name": "Headphones",
            "price": 149.99,
            "quantity": 2
          }
        ],
        "total_price": 1099.97,
        "order_date": "2024-02-08"
      },
      {
        "order_id": "789012",
        "products": [
          {
            "name": "Laptop",
            "price": 1299.99,
            "quantity": 1
          },
          {
            "name": "External Hard Drive",
            "price": 99.99,
            "quantity": 1
          }
        ],
        "total_price": 1399.98,
        "order_date": "2024-01-15"
      }
    ]
  }
}
'''

# Parse JSON
data = json.loads(json_data)

# Flatten JSON into a DataFrame
df_customer = pd.json_normalize(data['customer'], max_level=1)

# Print important parts
print("Customer Details:")
print(df_customer[['name', 'age', 'email']])
print("\nCustomer Address:")
print(df_customer[['address.city', 'address.country', 'address.zipcode']])

print("\nOrder Details:")
for order in data['customer']['orders']:
    df_order = pd.json_normalize(order, max_level=1)
    print("\nOrder ID:", order['order_id'])
    print("Order Date:", order['order_date'])
    print("Total Price:", order['total_price'])
    print("\nProduct Details:")
    print(df_order['products'])
