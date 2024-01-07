#!/usr/bin/python3
"""
    print the square
"""


def print_square(size):
    """ print the shape of a square"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    shape = ["#"*size for i in range(size)]
    for row in shape:
        print(row)
