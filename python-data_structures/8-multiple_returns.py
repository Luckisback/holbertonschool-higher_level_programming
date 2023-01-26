#!/usr/bin/python3
def multiple_returns(sentence):
    lg = len(sentence)
    fchar = sentence[0]
    if sentence is None:
        return
    else:
        tpl = (lg, fchar)
    return tpl
