#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    int_max = my_list[0]
    for i in my_list:
        if type(i) == int:
            if i > int_max:
                int_max = i
    return int_max            
