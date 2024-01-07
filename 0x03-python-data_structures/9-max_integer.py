#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        Return ("None")
    else:
        greater = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > greater:
                greater = my_list[i]
        return greater
