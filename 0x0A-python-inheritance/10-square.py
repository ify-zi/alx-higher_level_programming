#!/usr/bin/python3
"""
    square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Creation of class Square
    """

    def __init__(self, size):
        """
            initialise the Square clas
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            Overrides the area() of Rectangle
            and computes for square
        """
        return self.__size ** 2
