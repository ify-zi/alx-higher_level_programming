#!/usr/bin/python3
"""
    class of Rectangle
"""


class Rectangle:
    """
        Initializing Class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Instance creation variables
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            attr property getter
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """s
            object compare func
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

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

    def __str__(self):
        """
            prints the dimension attr of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ("\n".join([str(self.print_symbol)*self.__width
                              for rows in range(self.__height)]))

    def __repr__(self):
        """
            prints format for IDE or env to undertsand
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
            deletes instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
