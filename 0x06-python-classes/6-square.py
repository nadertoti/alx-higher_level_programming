#!/usr/bin/python3                                                               
"""Square module. """


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        
        """
        self.__size = size
        self.position = position
        
    @property
    def size(self):
        """property for the length of a side of this square.
        
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Area of the square.
        
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
    def area(self):
        """return."""
        return (self.__size * self.__size)
    
    def my_print(self):
        """prints the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="" for k in range(0, self.__size)]
            print("")
