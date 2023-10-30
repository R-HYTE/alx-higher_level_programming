#!/usr/bin/python3
"""  class Rectangle that defines a rectangle  """


class Rectangle:
    """ This class defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle instance """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter method for the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle """
        return 2 * (self.__width + self.__height)

