#!/usr/bin/python3
for i in range(90):
    if i == 89:
        print("{:02}".format(i), end="\n")
        break
    elif i in [10, 11, 20, 21, 30, 31, 32, 40, 41, 42, 43, 44,
            51, 52, 43, 54, 55, 60, 61, 62, 63, 64, 65, 66, 70,
            71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85,
            86, 87, 88]:
        continue
    print("{:02}".format(i), end=", ")
