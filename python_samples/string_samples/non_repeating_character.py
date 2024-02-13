"""
Non-Repeating Character (Python)
Implement a function that takes a string and returns the first character that does not appear twice or more.

Example:

"abacc" -> 'b' ('a' appears twice, and so does 'c')
"xxyzx" -> 'y' ('y' and 'z' are non-repeating characters, and 'y' appears first)
If there is no non-repeating character, return None.
"""

# Implement your function below.
def non_repeating(given_string):
    non_repeating_character = None
    print("input:",given_string)
    item_count_dict ={}
    for item in given_string:
        if item in item_count_dict.keys():
            item_count_dict[item]=item_count_dict[item]+1
        else:
            item_count_dict[item]= 1
    for key,value in item_count_dict.items():
        if value ==1:
            non_repeating_character = key
            break
    print(non_repeating_character)
    return non_repeating_character

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'