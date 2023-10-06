#!/usr/bin/python3
"""A Rectangle Class Definition"""


class Rectangle:
    """A Rectangle class definition
    Attribute:
        __width
        __height
    Methods: Will enter again"""
    number_of_instances = 0
    print_symbol = "#"

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
            Rectangle.number_of_instances += 1

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
            sym_str = str(self.print_symbol)if self.print_symbol else str(
                Rectangle.print_symbol)
            for i in range(self.height):
                my_str += (sym_str * self.width + "\n")
            return my_str.rstrip()

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Method called when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equal rectangle class comparator"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """A Class method that initializes an returns a square object"""
        return cls(size, size)
