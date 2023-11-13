#!/usr/bin/python3
""" This module inherits from the Base class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor for the Rectangle class '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ Rectange's width """
            return self.__width

        @width.setter
        def width(self, value):
            ''' Adjusting rectangle's width '''
            self.__width = value

        @property
        def height(self):
            """ Rectangle's height """
            return self.__height

        @height.setter
        def height(self, value):
            ''' Adjusting rectangle's height '''
            self.__height = value

        @property
        def x(self):
            """ Accessing the value of x """
            return self.__x

        @x.setter
        def x(self, value):
            ''' Adjusting the value of x '''
            self.__x = value

        @property
        def y(self):
            """ Accessing the value of y """
            return self.__y

        @y.setter
        def y(self, value):
            ''' Adjsuting the value of y '''
            self.__y = value
