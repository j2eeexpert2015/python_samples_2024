def reverse_string(input):
    temp=""
    for i in range(len(input)-1,-1,-1):
        temp=temp+input[i]
    print(temp)

def validate_pallindrome(input):
    if input == input[::-1]:
        print("Yes ")
    else:
        print("No")


#reverse_string("123456")
validate_pallindrome('12456')