#!/usr/bin/python3
""" Module for test Square class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import os
from unittest.mock import patch
import json


class TestSquare(unittest.TestCase):
    """Test class for the Square module."""

    def test_constructor(self):
        """Test the constructor of the Square class."""
        rect = Square(5, 2, 3, 1)
        self.assertEqual(rect.size, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_area(self):
        """Test the area() method of the Square class."""
        rect = Square(5)
        self.assertEqual(rect.area(), 25)

    def test_display(self):
        """Test the display() method of the Square class."""
        rect = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__() method of the Square class."""
        rect = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        """Test the update() method of the Square class."""
        rect = Square(5, 2, 3, 1)
        rect.update(7, 8, 4, 5)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.size, 8)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_kwargs(self):
        """Test the update() method of the Square class with **kwargs."""
        rect = Square(5, 2, 3, 1)
        rect.update(size=8, y=5, id=7)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.size, 8)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary() method of the Square class."""
        rect = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_json_string(self):
        """Test the to_json_string() method of the Square class."""
        rect_list = [Square(5, 2, 3, 1), Square(3, 1, 1, 2)]
        list_dictionaries = [rect.to_dictionary() for rect in rect_list]
        json_str = Square.to_json_string(list_dictionaries)
        expected_json = json.dumps(list_dictionaries)
        self.assertEqual(json_str, expected_json)

    def test_save_to_file(self):
        """Test the save_to_file() method of the Square class."""
        rect_list = [Square(5, 2, 3, 1), Square(3, 1, 1, 2)]
        filename = "Square.json"

        Square.save_to_file(rect_list)

        with open(filename, "r") as file:
            data = json.load(file)
            expected_data = [rect.to_dictionary() for rect in rect_list]
            self.assertEqual(data, expected_data)

        os.remove(filename)

    def test_from_json_string(self):
        """Test the from_json_string() method of the Square class."""
        json_str = """[{"id": 1, "size": 5, "x": 2, "y": 3},
        {"id": 2, "size": 3, "x": 1, "y": 1}]"""
        rect_list = Square.from_json_string(json_str)
        expected_list = [
                {'id': 1, 'size': 5, 'x': 2, 'y': 3},
                {'id': 2, 'size': 3, 'x': 1, 'y': 1}
                ]
        self.assertEqual(rect_list, expected_list)

    def test_create(self):
        """Test the create() method of the Square class."""
        rect_attributes = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        rect = Square.create(**rect_attributes)
        expected_rect = Square(5, 2, 3, 1)
        self.assertEqual(rect.to_dictionary(), expected_rect.to_dictionary())

    def test_load_from_file(self):
        """Test the load_from_file() method of the Square class."""
        rect_list = [Square(5, 2, 3, 1), Square(3, 1, 1, 2)]
        filename = "Square.json"

        Square.save_to_file(rect_list)

        loaded_rect_list = Square.load_from_file()
        self.assertEqual(len(loaded_rect_list), len(rect_list))

        for rect, expected_rect in zip(loaded_rect_list, rect_list):
            self.assertEqual(rect.to_dictionary(),
                             expected_rect.to_dictionary())

        os.remove(filename)
