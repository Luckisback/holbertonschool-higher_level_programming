#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multpl = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multpl.append(True)
        else:
            multpl.append(False)
    return multpl
