#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    Sum = 0
    _arg = 0
    _nb = (len(argv) - 1)
    for i in range(1, (_nb + 1)):
        _arg = int(argv[i])
        Sum = (Sum + _arg)
    print("{}".format(Sum))
