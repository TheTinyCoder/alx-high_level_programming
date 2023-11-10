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
        id (int: public instance attribute)
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
        """
        Updates values of instance attributes
        If args:
            (varied arguments treated as list) is present
            kwargs is ignored
        If length of args is zero:
            kwargs (named arguments treated as dict) is used
        """
        keys = ["id", "size", "x", "y"]
        if (len(args) > 0):
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for (k, v) in kwargs.items():
                if k in keys:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns dictionary representation of a Square"""
        a_dict = self.__dict__.copy()
        a_dict["size"] = a_dict.pop("_Rectangle__width")
        a_dict.pop("_Rectangle__height")
        a_dict["x"] = a_dict.pop("_Rectangle__x")
        a_dict["y"] = a_dict.pop("_Rectangle__y")
        return (a_dict)
