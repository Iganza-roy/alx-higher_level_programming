#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = [[i ** 2 for i in k] for k in matrix]
    return new_mtx


"""
or, using the map function:
return [list(map(lambda x: x ** 2, row)) for row in matrix]
"""
