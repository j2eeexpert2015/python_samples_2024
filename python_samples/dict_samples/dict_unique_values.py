"""
You are given a dictionary with a key-value of {string: number} where values in the dictionary
could be duplicates. You are required to extract the unique values from the dictionary where
the value occurred only once.
Return a list of values where they occur only once.
"""
def get_dict_unique_values(input_dict):
    unique_item_list =[]
    for k,v in input_dict.items():
        #print(f"key:{k},value:{v}")
        if v in unique_item_list:
            unique_item_list.remove(v)
        else:
            unique_item_list.append(v)
    print(f"Unique item:{unique_item_list}")

sample_dict = {1:"a",2:"b",3:"c",4:"a"}
get_dict_unique_values(sample_dict)