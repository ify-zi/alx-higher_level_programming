#!/usr/bin/python3
"""
    MyInt module
"""


class MyInt(int):
    """
        Instance of Int Object
    """

    def __eq__(self, b):
        """
            invert the == operator
        """
        return not super().__eq__(b)

    def __ne__(self, b):
        """
            inverts the != operator
        """
        return super().__eq__(b)
