#!/usr/bin/python3
def multiple_returns(sentence):
    lg = len(sentence)
    if sentence == "":
        fchar = None
    else:
        fchar = sentence[0]
        tpl = (lg, fchar)
    return tpl
