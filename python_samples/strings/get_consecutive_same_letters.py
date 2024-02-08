def get_consecutive_same_letters(input):
    string_length = len(input)
    for i in range(0,string_length):
        temp =[]
        while(i+1 <string_length and input[i]== input[i+1]):
            if(len(temp)==0):
                temp.append(input[i])
            temp.append(input[i])
            i= i+1
        if len(temp) > 0:
            print(temp)
            temp=[]
s ="aaaabcddd"
get_consecutive_same_letters(s)
