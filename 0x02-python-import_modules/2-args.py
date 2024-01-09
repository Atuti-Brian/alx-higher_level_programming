#!/usr/bin/python3
import sys

if __name__ == "__main__":

    m = len(sys.argv)
    plural = "s" if m == 1 or m > 2 else ""
    q = ":" if m > 1 else "."

    print("{:d} argument{}{}".format(m - 1, plural, q))

    for i in range(1, m):
        print("{:d}: {}".format(i, sys.argv[i]))
