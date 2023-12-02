#!/usr/bin/python3
def uppercase(str):
    result = ""
    for j in str:
        if ord(j) >= 97 and ord(j) <= 122:
            result += chr(ord(j) - 32)
        else:
            result += j
    print("{}".format(result))
