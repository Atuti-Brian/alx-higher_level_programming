#!/usr/bin/python3
import sys

if __name__ == "__main__":
    m = len(sys.argv)
    if m == 1:
        print("{}".format(m - 1))
    else:
        result = 0
        for i in range(1, m):
            result += int(sys.argv[i])
        print(result)
