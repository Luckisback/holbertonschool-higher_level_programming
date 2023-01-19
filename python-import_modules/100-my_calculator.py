#!/usr/bin/python3
from calculator_1 import (add, sub, mul, div)
from sys import argv

if __name__ == "__main__":

    lg = len(argv)
    operator = ["+", "-", "*", "/"]
    if (lg - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        oper = argv[2]
    if oper not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

    if oper == "+":
        print("{} {} {} = {}".format(a, oper, b, add(a, b)))
    elif oper == "-":
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    elif oper == "*":
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    elif oper == "/":
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
