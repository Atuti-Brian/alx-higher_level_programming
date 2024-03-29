#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
#        i += 1
    print()
    return printed
