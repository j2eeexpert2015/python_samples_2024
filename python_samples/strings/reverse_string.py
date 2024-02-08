def reverse_string(input):
    temp=""
    for i in range(len(input)-1,-1,-1):
        temp=temp+input[i]
    print(temp)

reverse_string("123456")