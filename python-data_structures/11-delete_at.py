#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    a = idx
    if my_list is None or a < 0:
        return
    elif a < 0:
        return my_list
    else:
        del my_list[a]
    return my_list
