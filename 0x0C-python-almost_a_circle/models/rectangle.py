#!/usr/bin/python3
"""
Module that contains the Rectangle class,
inherited from the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using the '#' character.
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        className = f"[{self.__class__.__name__}] "
        instance_id = f"({self.id}) "
        xy = f"{self.x}/{self.y} - "
        wh = f"{self.width}/{self.height}"

        return className + instance_id + xy + wh

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable length argument list containing attribute
            values in the order: id, width, height, x, y.
            **kwargs: Arbitrary keyword arguments containing attribute
            names and values.

        Note:
            The attributes are updated in the following order:
            id, width, height, x, y.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle's attributes.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        attrs_dict = {}

        for attr in attrs:
            attrs_dict[attr] = getattr(self, attr)

        return attrs_dict
