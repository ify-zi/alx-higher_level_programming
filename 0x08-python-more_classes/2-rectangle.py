#!/usr/bin/python3
"""
    class of Rectangle
"""


class Rectangle:
    """
        Initializing Class
    """

    def __init__(self, width=0, height=0):
        """
            Instance creation variables
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

    def area(self):
        """
            Calculate the area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculate the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
