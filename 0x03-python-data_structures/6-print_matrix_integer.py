#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        res = ""
        for n in r:
            res += "{:d}, ".format(n)
        print(res[:-2])
