#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    if my_list is None:
        return
    elif idx < 0:
        return my_list
    elif idx not in range(len(my_list)):
        return my_list
    else:
        copy_list = my_list[0:]
        copy_list[idx] = element
    return copy_list
