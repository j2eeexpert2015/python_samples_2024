"""
Adding Items to a List
Using append(): Adds an item to the end of the list.
Using insert(): Inserts an item at a specified position.
Using extend(): Adds all elements of a list (or any iterable) to the end of the current list.
"""
# Sample list
product_list = ['T-shirt', 'Jeans']

# Adding items
product_list.append('Sneakers')  # Adds 'Sneakers' to the end
"""
When you use the insert() method on a Python list to insert an item at a specific index, 
the existing item at that index, and all subsequent items, are shifted one position to the right. 
The insert() method does not overwrite or remove the existing item; it merely displaces it.
"""
product_list.insert(1, 'Hats')  # Inserts 'Hats' at index 1
product_list.extend(['Socks', 'Scarves'])  # Adds 'Socks' and 'Scarves' to the end

print(product_list)
"""
Updating Items in a List
To update an item, assign a new value to the desired index.
"""
# Sample list
product_list = ['T-shirt', 'Jeans', 'Sneakers']

# Updating an item
product_list[1] = 'Shorts'  # Updates 'Jeans' to 'Shorts'

print(product_list)
"""
Removing Items from a List
Using remove(): Removes the first occurrence of a specified item.
Using pop(): Removes the item at the specified position and returns it. If no index is specified, pop() removes and returns the last item in the list.
Using del: Removes an item or slices from the list or deletes the entire list.
Using clear(): Empties the list.
"""
# Sample list
product_list = ['T-shirt', 'Jeans', 'Sneakers', 'Hats']

# Removing items
product_list.remove('Jeans')  # Removes 'Jeans'
popped_item = product_list.pop(1)  # Removes and returns the item at index 1 ('Sneakers')
del product_list[1]  # Deletes 'Hats' at index 1
product_list.clear()  # Clears the list

print(product_list)  # This will print an empty list
