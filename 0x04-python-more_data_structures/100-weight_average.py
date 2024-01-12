#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    add = 0
    den = 0
    for prod, weight in my_list:
        add += prod * weight
        den += weight
    if den == 0:
        return 0
    avg = add / den
    return avg
