#!/usr/bin/python3
"""
Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        className = f"[{self.__class__.__name__}] "
        instance_id = f"({self.id}) "
        xy = f"{self.x}/{self.y} - "
        size = f"{self.width}"

        return className + instance_id + xy + size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable length argument list containing attribute
            values in the order: id, size, x, y.
            **kwargs: Arbitrary keyword arguments containing attribute
            names and values.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square's attributes.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
