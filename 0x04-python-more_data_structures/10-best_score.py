#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    greatest_key = None
    greatest_val = float('-inf')

    for key, value in a_dictionary.items():
        if value > greatest_value:
            greatest_key = key
            greatest_value = value
                
    return greatest_key
