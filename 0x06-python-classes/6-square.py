#!/usr/bin/python3

"""Square module. """


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor."""
        self.__size = size
        self.__position = position  # Use a different name for the instance attribute

    @property
    def size(self):
        """Property for the length of a side of this square."""
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
        """Position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Use a different name for the instance attribute

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")

if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()
