#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or (my_list[idx] == idx):
        return (None)
    elif idx > len(my_list) or idx == len(my_list):
        return (None)
    elif idx >= 0 and idx <= len(my_list):
        return my_list[idx]
