# Creating a Product Catalog
product_catalog = {}  # Empty product catalog
product_catalog = {101: 'T-shirt', 102: 'Jeans'}  # Catalog with product ID as keys
product_catalog = {'name': 'Sneakers', 'price': 59.99}  # Product details
product_catalog = dict({101: 'T-shirt', 102: 'Jeans'})  # Using dict() for product catalog

# Accessing Product Details
print(product_catalog['name'])  # Accessing product name using key
print(product_catalog.get(101))  # Accessing product using get()

# Adding and Updating Products
product_catalog['quantity'] = 150  # Adding a new key-value pair for quantity
product_catalog['price'] = 64.99  # Updating the price of the product

# Removing Products
del product_catalog['quantity']  # Remove a product attribute using del
product_catalog.pop(101)  # Remove a product using pop()
product_catalog.popitem()  # Removes the last inserted item
product_catalog.clear()  # Remove all products

# Product Catalog Methods
product_ids = product_catalog.keys()  # Returns a list containing the catalog's product IDs
prices = product_catalog.values()  # Returns a list containing the catalog's prices
items = product_catalog.items()  # Returns a list of tuple pairs (product ID, detail)
product_catalog.copy()  # Returns a copy of the product catalog
product_catalog.fromkeys(['SKU', 'Description'], 'N/A')  # Create a new catalog with keys and a default value
product_catalog.setdefault('SKU', None)  # Get the value of a SKU if in catalog, else insert SKU with a value
product_catalog.update({'discount': 10})  # Updates the catalog with new discount information

# Iterating Through Product Catalog
for product_id in product_catalog:
    print(product_id, product_catalog[product_id])  # Iterating through product IDs

for product_id, detail in product_catalog.items():
    print(product_id, detail)  # Iterating through product ID and details
