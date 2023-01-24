#!/usr/bin/python3
def no_c(my_string):
    copy_string = ""
    if my_string is None:
        return
    else:
        for i in range(0, len(my_string)):
            if my_string[i] not in ['c', 'C']:
                copy_string += my_string[i]
        return copy_string
