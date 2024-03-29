#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
#    op = sys.argv[2]
#    a = int(sys.argv[1])
#    b = int(sys.argv[3])
    operators = ['+', '-', '*', '/']
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
