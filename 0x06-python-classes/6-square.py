#!/usr/bin/python3
""" square class"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initialize a square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property  # getter method
    def size(self):
        """ returns a squares size """
        return self.__size

    @size.setter  # setter method
    def size(self, value):
        """ sets a squares size value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Sets posiion value """
        return self._position

    @position.setter
    def position(self, value):
        """ aets position values """
        if not isinstance(value, tuple) or len(value) != 2 \
        or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value  # HERE HERE

    def area(self):
        """
        Finds the area of square
        Returns:
            float: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the char #
        if size == 0 prints empty line
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
