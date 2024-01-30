#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Defining the matrix_divide function

    Args:
    matrix (list): A list of lists containing int/floats
    div (int/float): the divisor

    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(j, list) for j in matrix) or
            not all((isinstance(i, int) or isinstance(i, float))
                    for i in [n for j in matrix for n in j])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of a matrix must have a same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    res_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return res_matrix
