#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,)
    if len(tuple_b) < 2:
        tuple_b += (0,)

    tup1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    tup2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tup3 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tup4 = tuple_b[1] if len(tuple_b) >= 2 else 0
    res = (tup1 + tup3, tup2 + tup4)
    return res
