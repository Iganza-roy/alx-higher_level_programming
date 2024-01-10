#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = [[i ** 2 for i in k] for k in matrix]
    return new_mtx
