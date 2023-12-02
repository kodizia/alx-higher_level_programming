#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if ord(j) >= 97 and ord(j) <= 122:
            print("{}".format(chr(ord(j) - 32)), end='')
        else:
            print("{}".format(j), end="")
