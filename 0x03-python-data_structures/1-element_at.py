#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return 'None'
    return my_list[idx]


'''
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            return my_list[idx]
'''
