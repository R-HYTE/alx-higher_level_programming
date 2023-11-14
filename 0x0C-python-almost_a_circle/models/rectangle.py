#!/usr/bin/python3
""" This module inherits from the Base class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor for the Rectangle class '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for Rectange's width """
        return self.__width

    @width.setter
    def width(self, value):
        ''' Adjusting rectangle's width '''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ Rectangle's height getter """
        return self.__height

    @height.setter
    def height(self, value):
        ''' Adjusting rectangle's height '''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ Accessing the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        ''' Adjusting the value of x '''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """ Accessing the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        ''' Adjusting the value of y '''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, attribute_name, value, non_negative=True):
        ''' Validating the value '''
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if non_negative and value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
        elif not non_negative and value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def area(self):
        ''' Computes the area of the rectangle '''
        return self.width * self.height

    def display(self):
        ''' Dispalys the rectangle with # character '''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        ''' String representation of the Rectangle '''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        ''' Assigns positional and keyword arguments to attributes '''
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        elif kwargs:
            # If **kwargs is not empty, update attributes
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
