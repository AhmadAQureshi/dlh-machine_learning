#!/usr/bin/python3
"""This module defines a Square class with printable instance behavior."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with size and position.

        Args:
            size: The size of the square.
            position: The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: The new position of the square.

        Raises:
            TypeError: If position is invalid.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        print(self)

    def __str__(self):
        """Return the square as a printable string."""
        if self.__size == 0:
            return ""

        square = "\n" * self.__position[1]

        for i in range(self.__size):
            square += " " * self.__position[0]
            square += "#" * self.__size

            if i != self.__size - 1:
                square += "\n"

        return square