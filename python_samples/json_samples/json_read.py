import json

# The path to your JSON file
file_path = 'sample.json'

# Reading the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Accessing and printing specific parts of the JSON structure
for user in data['users']:
    print(f"User ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print("Address:")
    print(f"  Street: {user['address']['street']}")
    print(f"  City: {user['address']['city']}")
    print(f"  Zipcode: {user['address']['zipcode']}")
    print("Contact:")
    print(f"  Home: {user['contact']['home']}")
    print(f"  Mobile: {user['contact']['mobile']}")
    print("----------")
