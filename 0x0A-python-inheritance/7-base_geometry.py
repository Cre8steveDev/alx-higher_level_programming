#!/usr/bin/python3

"""Create a Geometry Class"""


class BaseGeometry():
    """A Base Geometry class"""

    def area(self):
        """Un-implemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
