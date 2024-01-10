#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_keys = sorted(a_dictionary.keys())

    for i in my_keys:
        print("{}: {}".format(i, a_dictionary[i]))
