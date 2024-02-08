"""
One Away Strings (Python)
Write a function that takes two strings and returns True if they are one away from each other.

They are one away from each other if a single operation (changing a character, deleting a character or adding a character) will change one of the strings to the other.

Examples:

"abcde" and "abcd" are one away (deleting a character).
"a" and "a" are one away (changing the only character 'a' to the equivalent character 'a').
"abc" and "bcc" are NOT one away. (They are two operations away.)
"""
# Implement your function below.
def is_one_away(s1, s2):
    result = False
    length_difference = abs(len(s1) - len(s2))
    if length_difference<=1:
        if len(s1) == len(s2):
            for i in range(0,len(s1)):
                if s1[i] !=s2[i]:
                    s3 = s1[:i] + s2[i] + s1[i + 1:]
                    s1 = s3
                    break
            if s1==s2:
                print("Success !!!!!!!!!!1")
        else:
            min_length = len(s1)
            string_to_be_modified = s1
            s3=""
            if len(s1) > len(s2) :
                min_length = len(s2)
                string_to_be_modified = s2
            for i in range(0,min_length):
                if s1[i] !=s2[i]:
                    s3 = string_to_be_modified[:i] + string_to_be_modified[i] + string_to_be_modified[i + 1:]
            if s1 == s3 or s2 == s3 :
                print("Success!!!!!!")
    return result

# NOTE: The following input values will be used for testing your solution.
is_one_away("abde", "abdc")  # should return True

is_one_away("abcde", "abcd")  # should return True
"""
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
"""