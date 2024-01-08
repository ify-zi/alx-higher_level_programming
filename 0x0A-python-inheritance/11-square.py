#!/usr/bin/python3
"""
    Square Module v.1.2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        An Object of a square
    """
    def __init__(self, size):
        """
            initializing of the square object
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            computes the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
            informal string reepresentation of the square
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
