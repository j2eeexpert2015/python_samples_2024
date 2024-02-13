#Custom Functions Example
"""
This code defines a function count_a that counts the number of occurrences of the letter 'a' in a string.
It then sorts the list words based on the number of 'a's in each word, from the fewest to the most.
"""
def count_a(s):
    return s.count('a')

words = ['banana', 'apple', 'grape', 'avocado']
sorted_words = sorted(words, key=count_a)
#Lambda Functions Example
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

