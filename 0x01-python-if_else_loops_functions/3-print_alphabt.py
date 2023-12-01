#!/usr/bin/python3
for _ in range(97, 123):
    if _ == 101 or _ == 113:
        continue
    else:
        print("{}".format(chr(_)), end='')
