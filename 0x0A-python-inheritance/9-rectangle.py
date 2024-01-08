#!/usr/bin/python3
"""
    Rectangle modified
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        creation of rectangle sub of BG
    """

    def __init__(self, width, height):
        """
            define param of Rectangle
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            computes area
        """
        return self.__width * self.__height

    def __str__(self):
        """
            prints a formatted text
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
