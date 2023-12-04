#!/usr/bin/python3
"""Module for  basegeometry class method."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Subclass display a rectangle."""
    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size =size
        super().__init__(size, size)
    
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
