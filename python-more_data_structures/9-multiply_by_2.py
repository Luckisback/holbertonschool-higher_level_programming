#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_multi = a_dictionary.copy()
    for key, value in dic_multi.items():
        dic_multi[key] = value * 2
    return dic_multi
