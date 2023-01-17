#!/usr/bin/python3
def remove_char_at(str, n):
    lg = len(str)
    _str = list(str)

    if n > lg:
        pass
    elif n < 0:
        pass
    elif n >= 0:
        _str.pop(n)
    
    my_str = "".join(_str)
    return (my_str)
