s1 ="abcde"
s2="123456789"
def concat_alternate_character(s1,s2):
    s1_length = len(s1)
    s2_length= len(s2)
    length_difference = abs(s1_length-s2_length)
    final_string = ""
    additional_string=""
    if length_difference > 0:
        if s1_length > s2_length:
            additional_string = s1[s2_length:]
        else:
            additional_string = s2[s1_length]
    for i in range(s1_length):
        final_string = final_string+s1[i]+s2[i]
    final_string = final_string+additional_string
    print(final_string)

concat_alternate_character(s1,s2)