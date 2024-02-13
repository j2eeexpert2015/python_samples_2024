def is_balanced(input):
    mapping_dict = {"{":"}","(":")","[":"]"}
    mid_index = int(len(input)/2)
    balanced = False
    for i in range(mid_index):
        if input[i] in mapping_dict.keys() and input[len(input)-1 -i]==mapping_dict.get(input[i]):
            balanced=True
        else:
            balanced=False
            print("issue at index:" ,i)
            break
    print("Result:",balanced)

is_balanced("({[]})")
