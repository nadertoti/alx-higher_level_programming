#!/usr/bin/python3
    """Defines a class Rectangle

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
class Rectangle:
    """Representation of a rectangle
    """
    def __init__(self, width=0, height=0):
        """Intitialize the rectangle.

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width
    
    @property
    def width(self):
        """getter for the private instance attribute width

        Returns:
            _type_: _description_
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for the private instance attribute width

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if TypeError(value) is not int:
            raise TypeError("width must be an intege")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """getter for the private instance attribute height

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
