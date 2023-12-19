#!/usr/bin/python3
"""Defining a class"""


class Square:
    """create a class
    Attributes:
        __size (int): a private class attr
    """

    def __init__(self, size=0):
        """initialise the class
        Args:
            size (int): args passed at create
        Return: None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be <= 0")
        self.__size = int(size)

    def area(self):
        """finds area of size
        Args:
            __size (int):class attr
        Return: returns the area of size
        """
        area = self.__size ** 2
        return area
