#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square: inherits from Rectangle
    Attributes:
        size (int: private instance attribute)
        x (int: private instance attribute)
        y (int: private instance attribute)
        id (int: inherited attribute)
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        if self.integer_validator("width", size) is None:
            self.width = size
            self.height = size

    def __str__(self):
        """Returns informal string representation of square instance"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """Updates values of instance attributes"""
        order = ["id", "_Rectangle__width",
                 "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
        if (len(args) > 0):
            j = 0
            for i in range(len(args)):
                if i == 1:
                    self.size = args[i]
                    j += 2
                    continue
                self.__dict__[order[j]] = args[i]
                j += 1
        else:
            keys = ["id", "width", "height", "x", "y"]
            for (k, v) in kwargs.items():
                if k == "size":
                    self.size = v
                elif k in keys:
                    self.__dict__[order[keys.index(k)]] = v
