# Sample nested dictionary
nested_dict = {
    'key1': {
        'subkey1': 'value1',
        'subkey2': 'value2'
    },
    'key2': {
        'subkey3': 'value3',
        'subkey4': 'value4'
    }
}

# Reading from the nested dictionary
print("Reading from the nested dictionary:")
print("Value corresponding to key1: ", nested_dict['key1'])
print("Value corresponding to key2: ", nested_dict['key2'])
print("Value corresponding to subkey1: ", nested_dict['key1']['subkey1'])
print("Value corresponding to subkey4: ", nested_dict['key2']['subkey4'])

# Updating the nested dictionary
print("\nUpdating the nested dictionary:")
nested_dict['key1']['subkey1'] = 'new_value1'
print("Updated value corresponding to subkey1: ", nested_dict['key1']['subkey1'])
nested_dict['key2']['subkey5'] = 'value5'
print("Newly added subkey5 in key2: ", nested_dict['key2']['subkey5'])

# Deleting from the nested dictionary
print("\nDeleting from the nested dictionary:")
del nested_dict['key2']['subkey4']
print("Deleted subkey4 from key2: ", nested_dict['key2'])
del nested_dict['key1']
print("Deleted key1: ", nested_dict)

# Other operations
# Check if a key exists
if 'key1' in nested_dict:
    print("\n'key1' exists in the nested dictionary.")
else:
    print("\n'key1' does not exist in the nested dictionary.")

# Get all keys at a specific level
print("\nAll keys at the top level:", nested_dict.keys())
print("All keys at the second level of key2:", nested_dict['key2'].keys())

# Get all values
print("\nAll values:", nested_dict.values())

# Get all items
print("\nAll items:", nested_dict.items())
