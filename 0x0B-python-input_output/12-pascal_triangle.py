#!/usr/bin/python3

"""This defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    This represents Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    Returns an empty list if n <= 0
    Args:
        n: number of rows
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trn = triangle[-1]
        tmpy = [1]
        for i in range(len(trn) - 1):
            tmpy.append(trn[i] + trn[i + 1])
        tmpy.append(1)
        triangle.append(tmpy)
    return triangle

# Alternative implementation:


"""
def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j]
        for j in range(i + 1)]
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))
"""
