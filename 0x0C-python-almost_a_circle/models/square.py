#!/usr/bin/python3
"""
    Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class is Instacne of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            constructor function
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print out string format"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """attr getter"""
        return self.width

    @size.setter
    def size(self, value):
        """attr stter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """setting variable arguments"""

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """return dictionary of attr"""
        attr_dict = {}
        attr_dict = {
                    "id": getattr(self, "id"), "x": getattr(self, "x"),
                    "size": getattr(self, "size"), "y": getattr(self, "y")}
        return attr_dict
