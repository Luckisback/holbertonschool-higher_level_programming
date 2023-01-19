#!/usr/bin/python3
from sys import argv
_nb = (len(argv) - 1)
if _nb == 0:
    print("{} arguments.".format(_nb))
if _nb == 1:
    print("{} argument:".format(_nb))
if _nb > 1:
    print("{} arguments:".format(_nb))
for i in range(1, (_nb + 1)):
    print("{}: {}".format(i, argv[i]))
