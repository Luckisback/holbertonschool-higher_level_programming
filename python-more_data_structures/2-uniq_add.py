#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    list_uniq = list(set(my_list))
    for i in list_uniq:
        add = add + i
    return add
