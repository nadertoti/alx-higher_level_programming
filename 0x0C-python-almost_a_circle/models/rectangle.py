#!/usr/bin/python3
"""Module for rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constroctor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """height of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """height of the rectangle."""
        self.__width = value
    
    @property
    def height(self):
        """height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """height of the rectangle."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """height of the rectangle."""
        self.__x = value
    
    @property
    def y(self):
        """height of the rectangle."""
        return self.__y
    
    @y.setter
    def y(self, value):
        """height of the rectangle."""
        self.__y = value
