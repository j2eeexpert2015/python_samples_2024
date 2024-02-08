# Import necessary modules
import array
import itertools
from collections import deque
from functools import reduce

# This script serves as a reference for various list operations in Python,
# demonstrating creation, manipulation, and advanced techniques.

# 1. Creating Arrays
my_list = [1, 2, 3, 4]  # Using list
my_array = array.array('i', [1, 2, 3, 4])  # Using array module for type-specific array

# 2. Accessing Elements
element = my_list[0]  # Access the first element

# 3. Adding Elements
my_list.append(5)  # Append an element to the end
my_list.extend([6, 7])  # Extend the list with multiple elements
my_list = my_list + [8, 9]  # Concatenate lists

# 4. Removing Elements
my_list.remove(1)  # Remove the first occurrence of 1
popped_element = my_list.pop(2)  # Remove and return the element at index 2

# 5. Updating Elements
my_list[0] = 10  # Update the first element

# 6. Iterating Over the List
for element in my_list:
    print(element)

# Additional Operations

# Counting Occurrences
occurrences = my_list.count(2)

my_list = [10, 20, 30, 40, 50]

# Check if an element is in the list and get its index
element = 30

if element in my_list:
    index_position = my_list.index(element)
    print(f"Element found at index: {index_position}")
else:
    print("Element not found in the list")


# Inserting Elements
my_list.insert(1, 'a')

# List to String Conversion
my_str_list = ['Hello', 'world']
my_str = ' '.join(my_str_list)

# Flattening a List
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
flattened_itertools = list(itertools.chain.from_iterable(nested_list))

# Copying Lists
list_copy = my_list.copy()
list_copy2 = my_list[:]

# List as Stack
stack = []
stack.append('a')  # Push
stack.pop()  # Pop

# List as Queue
queue = deque(['a', 'b', 'c'])
queue.append('d')  # Enqueue
queue.popleft()  # Dequeue

# Filtering
even_numbers = [x for x in my_list if x % 2 == 0]
even_numbers_filter = list(filter(lambda x: x % 2 == 0, my_list))

# Mapping
squared = [x**2 for x in my_list]
squared_map = list(map(lambda x: x**2, my_list))

# Reducing
sum = reduce(lambda x, y: x + y, my_list)

# Zip and Unzip Lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
unzipped = list(zip(*zipped))


