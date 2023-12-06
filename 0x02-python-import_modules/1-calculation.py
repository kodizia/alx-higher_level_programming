#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))  # 10 + 5 = 15
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))  # 10 - 5 = 5
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))  # 10 * 5 = 50
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))  # 10 / 5 = 2
