#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle: inherits from Base
    Attributes:
        width (int: private instance attribute)
        height (int: private instance attribute)
        x (int: private instance attribute)
        y (int: private instance attribute)
        id (int: public instance attribute)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """
        Validates the parameter 'value'
        Args:
            name (str): name of value
            value (int)
        Raises:
            TypeError if value is not an integer
            ValueError if value is less than 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0 and name in ('width', 'height'):
            raise ValueError(name + " must be > 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if self.integer_validator("width", width) is None:
            self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if self.integer_validator("height", height) is None:
            self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if self.integer_validator("x", x) is None:
            self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if self.integer_validator("y", y) is None:
            self.__y = y

    def area(self):
        """
        Computes area of a rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """Prints in stdout a rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Returns informal string representation of rectangle instance"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Updates values of instance attributes
        If args:
            (varied arguments treated as list) is present
            kwargs is ignored
        If length of args is zero:
            kwargs (named arguments treated as dict) is used
        """
        order = ["id", "_Rectangle__width",
                 "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
        if (len(args) > 0):
            for i in range(len(args)):
                self.__dict__[order[i]] = args[i]
        else:
            keys = ["id", "width", "height", "x", "y"]
            for (k, v) in kwargs.items():
                if k in keys:
                    self.__dict__[order[keys.index(k)]] = v

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle"""
        a_dict = self.__dict__
        a_dict["width"] = a_dict.pop("_Rectangle__width")
        a_dict["height"] = a_dict.pop("_Rectangle__height")
        a_dict["x"] = a_dict.pop("_Rectangle__x")
        a_dict["y"] = a_dict.pop("_Rectangle__y")
        return (a_dict)
