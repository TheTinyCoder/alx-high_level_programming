#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square class

    Attributes:
        __size (int): length of the square
        __position (tuple of 2 positive int): position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size

        Returns: size of Square
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        Getter method for position

        Returns: position of Square
        """
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Computes area of Square

        Returns: area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        size, position = self.__size, self.__position
        if (size == 0):
            print()
        else:
            for i in range(position[1]):
                print()
            for i in range(size):
                print(" " * position[0], end="")
                print("#" * size, end="")
                print()

    def __str__(self):
        """
        Defines how instance of Square will be printed on print()
        """
        size, position = self.size, self.position
        if (size == 0):
            square_string = ""
        else:
            square_string = (("\n" * position[1]) + (((" " * position[0])
                             + ("#" * size) + "\n") * size))
        return (square_string)
