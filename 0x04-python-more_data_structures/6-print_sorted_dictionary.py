#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_dict = list(a_dictionary.keys())
    keys_dict.sort()
    for key in keys_dict:
        print("{}: {}".format(key, a_dictionary.get(key)))
