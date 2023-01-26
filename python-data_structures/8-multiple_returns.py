#!/usr/bin/python3
def multiple_returns(sentence):
    lg = len(sentence)
    if len(sentence) == 0:
        tpl = (0, None)
    else:
        fchar = sentence[0]
        tpl = (lg, fchar)
    return tpl
