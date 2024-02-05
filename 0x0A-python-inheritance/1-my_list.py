#!/usr/bin/python3
"""
class that inherits from list
"""


class MyList(list):
    """
    Defining the function
    """
    def print_sorted(self):
        """
        Public instance method: def print_sorted(self): that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
