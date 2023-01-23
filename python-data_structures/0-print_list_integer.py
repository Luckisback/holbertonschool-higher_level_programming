#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for idx in range(0, len(my_list)):
        if my_list[idx] != int(my_list[idx]):
            pass
        print("{:d}".format(my_list[idx]))
