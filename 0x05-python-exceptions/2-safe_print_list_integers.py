#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            cnt += 1
        except(TypeError, ValueError):
            continue
    print("")
    return(cnt)

