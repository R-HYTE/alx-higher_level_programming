#!/usr/bin/python3
"""A LockedClass class"""


class LockedClass:
    """
    Restricts the creation of instance attributes to a predefined set,
    preventing the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ("first_name", )

    def __init__(self):
        """Creates new instances of Locked Class."""
        self.first_name = "first_name"
