#!/usr/bin/python3
"""A Rectangle Class Definition"""


class Rectangle:
    """A Rectangle class definition
    Attribute:
        __width
        __height
    Methods: Will enter again"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Width Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter Function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height Property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter Function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimieter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """String representation of the class"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            my_str = ""
            for i in range(self.height):
                my_str += "#" * self.width + "\n"
            return my_str.rstrip()

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Method called when instance is deleted"""
        print("Bye rectangle...")
