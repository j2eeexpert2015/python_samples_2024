def add(a, b):
    return a + b

def greet(name):
    greeting = "Hello, " + name
    return greeting

add = lambda a, b: a + b
greet = lambda name: "Hello, " + name

#map() Function with Lambda vs. Regular Function
#Using Lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#Using Regular Function:
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#filter() Function with Lambda vs. Regular Function
#Using Lambda:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

def is_even(x):
    return x % 2 == 0

#Using Regular Function:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

