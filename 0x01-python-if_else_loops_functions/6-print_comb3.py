#!/usr/bin/python3
for _ in range(0, 10):
    for j in range(_ + 1, 10):
        if _ == 8 and j == 9:
            print("{}{}".format(_, j))
        else:
            print("{}{}".format(_, j), end=', ')
