#!/usr/bin/python3
"""
    Inheritance of class list
"""


class MyList(list):
    """
        class of parent class list
    """

    def print_sorted(self):
        """returns a sorted list"""
        print(sorted(self))
