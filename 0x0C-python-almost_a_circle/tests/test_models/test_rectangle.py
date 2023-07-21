#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import os
import json
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Test class for the Rectangle module."""

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_area(self):
        """Test the area() method of the Rectangle class."""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test the display() method of the Rectangle class."""
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__() method of the Rectangle class."""
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        """Test the update() method of the Rectangle class."""
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(7, 8, 9, 4, 5)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_update_kwargs(self):
        """Test the update() method of the Rectangle class with **kwargs."""
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(width=8, height=9, y=5, id=7)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary() method of the Rectangle class."""
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_json_string(self):
        """Test the to_json_string() method of the Rectangle class."""
        rect_list = [Rectangle(5, 10, 2, 3, 1), Rectangle(3, 6, 1, 1, 2)]
        list_dictionaries = [rect.to_dictionary() for rect in rect_list]
        json_str = Rectangle.to_json_string(list_dictionaries)
        expected_json = json.dumps(list_dictionaries)
        self.assertEqual(json_str, expected_json)

    def test_save_to_file(self):
        """Test the save_to_file() method of the Rectangle class."""
        rect_list = [Rectangle(5, 10, 2, 3, 1), Rectangle(3, 6, 1, 1, 2)]
        filename = "Rectangle.json"

        Rectangle.save_to_file(rect_list)

        with open(filename, "r") as file:
            data = json.load(file)
            expected_data = [rect.to_dictionary() for rect in rect_list]
            self.assertEqual(data, expected_data)

        os.remove(filename)

    def test_from_json_string(self):
        """Test the from_json_string() method of the Rectangle class."""
        json_str = """[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3},
        {"id": 2, "width": 3, "height": 6, "x": 1, "y": 1}]"""
        rect_list = Rectangle.from_json_string(json_str)
        expected_list = [
                {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3},
                {'id': 2, 'width': 3, 'height': 6, 'x': 1, 'y': 1}
                ]
        self.assertEqual(rect_list, expected_list)

    def test_create(self):
        """Test the create() method of the Rectangle class."""
        rect_attributes = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_attributes)
        expected_rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.to_dictionary(), expected_rect.to_dictionary())

    def test_load_from_file(self):
        """Test the load_from_file() method of the Rectangle class."""
        rect_list = [Rectangle(5, 10, 2, 3, 1), Rectangle(3, 6, 1, 1, 2)]
        filename = "Rectangle.json"
        Rectangle.save_to_file(rect_list)

        loaded_rect_list = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rect_list), len(rect_list))

        for rect, expected_rect in zip(loaded_rect_list, rect_list):
            self.assertEqual(rect.to_dictionary(),
                             expected_rect.to_dictionary())

        os.remove(filename)
