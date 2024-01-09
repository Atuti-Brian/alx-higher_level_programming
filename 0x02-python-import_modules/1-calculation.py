#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    g = 10
    h = 5

    print("{} + {} = {}".format(g, h, add(g, h)))
    print("{} - {} = {}".format(g, h, sub(g, h)))
    print("{} * {} = {}".format(g, h, mul(g, h)))
    print("{} / {} = {}".format(g, h, div(g, h)))
