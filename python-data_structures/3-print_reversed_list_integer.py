#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = -1
    if my_list ==None:
        return
    for i in range(len(my_list)):
        if my_list[idx] != int(my_list[idx]):
            pass
        print("{:d}".format(my_list[idx]))
        idx = idx - 1
