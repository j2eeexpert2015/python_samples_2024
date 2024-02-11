import pandas as pd

# Sample retail data
data = {
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['T-shirt', 'Jeans', 'Shoes', 'Sunglasses', 'Hat'],
    'Category': ['Apparel', 'Apparel', 'Footwear', 'Accessories', 'Accessories'],
    'Price': [20.99, 34.99, 49.99, 15.99, 9.99],
    'Quantity': [100, 50, 80, 120, 200]
}

# Creating DataFrame
retail_df = pd.DataFrame(data)

# Displaying the DataFrame
print("Retail DataFrame:")
print(retail_df)
print()

# Filtering data
print("Filtering data (Apparel category):")
apparel_df = retail_df[retail_df['Category'] == 'Apparel']
print(apparel_df)
print()

# Searching data
print("Searching for products with price less than $25:")
cheap_products_df = retail_df[retail_df['Price'] < 25]
print(cheap_products_df)
print()

# Sorting data
print("Sorting data by price in descending order:")
sorted_df = retail_df.sort_values(by='Price', ascending=False)
print(sorted_df)
print()

# Aggregating data
print("Aggregating data (total quantity and total price by category):")
agg_df = retail_df.groupby('Category').agg({'Quantity': 'sum', 'Price': 'sum'})
print(agg_df)
print()

# Other scenarios
# Accessing specific rows or columns
print("Accessing specific rows or columns:")
print("First 3 rows:")
print(retail_df.head(3))
print("Product names:")
print(retail_df['ProductName'])
