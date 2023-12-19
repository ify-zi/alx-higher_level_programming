#!/usr/bin/python3
"""defining class square"""


class Square:
    """class of square
    Attributes:
        __size (int): size of class
    """
    def __init__(self, size=0):
        """Initializing class
        Args:
            size (int): size of class
        Return: None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)
