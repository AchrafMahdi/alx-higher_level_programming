#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for i in matrix:
        new_matrix = map(lambda n: n**2, i)
        output.append(list(new_matrix))
    return output
