#!/usr/bin/python3
"""Defining a class"""


class Square:
    """defining a class square

    Attributes:
        __size (int): a private attribute of square size
    """
    def __init__(self, size):
        """Initailise the class
        Args:
            size (int): the size of the object
        Return: None
        """
        self.__size = size
