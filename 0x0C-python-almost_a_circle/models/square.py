#!/usr/bin/python3
""" This module inherits from the Rectangle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor for the Square class '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' String representation of the Square '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Accessing the value of size """
        return self.width

    @size.setter
    def size(self, value):
        ''' Adjusting the value of size '''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        ''' Updates attributes based on arguments '''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            # If **kwargs is not empty, update attributes using keyword arguments
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
