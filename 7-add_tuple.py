#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    tuple_x = tuple_a + (0, 0)
    tuple_y = tuple_b + (0, 0)

    tuple_c = tuple_x[0] + tuple_y[0], tuple_x[1] + tuple_y[1]
    return tuple_c


'''
    tuple_c = ()
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_c
    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        tuple_a[1] = 0
        tuple_a[1] = 0
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_c
'''
