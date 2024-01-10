#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(val ** 2)
        sq_matrix.append(new_row)
    return sq_matrix


'''        SIMPLER WAY OF DOING
def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in row] for row in matrix]
    return new_matrix
'''
