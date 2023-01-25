#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tpl_a = list(tuple_a)
    tpl_b = list(tuple_b)
    tplist = []
    for i in range(len(tuple_a)):
        if len(tpl_a) > len(tpl_b):
            tpl_b.append(0)
        tplist.append(tpl_a[i] + tpl_b[i])
    new_tpl = tuple(tplist)
    return new_tpl
