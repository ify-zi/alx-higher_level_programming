#!/usr/bin/python3
"""
    this class defines a rectangle
"""


class Rectangle:
    """
        Rectangle Object
    """

    def __init__(self, width=0, height=0):
        """
            param constructor
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
            property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """attr setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            attr(height) setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
