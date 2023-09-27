#!/usr/bin/python3

"""A Square class"""


class Square:
    """An ampty class Square that defines a square.
    It currently has no attributes nor properties.
    """

    def __init__(self, size=0):
        """Initialization method of the class
                Args:
                        size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square instance
                Returns:
                        Integer: Square of the size
                """
        return (self.__size ** 2)
