#!/usr/bin/python3
"""
    class inheritance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        child class of Base Geomtry
    """

    def __init__(self, width, height):
        """
            instantiation of Rectangle class
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
