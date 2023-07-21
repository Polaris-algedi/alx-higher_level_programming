#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """Set up the test environment."""
        Base._Base__nb_objects = 0
        self.base_instance = Base()
        self.list_objs = [self.base_instance]

    def tearDown(self):
        """Tear down the test environment."""
        self.base_instance = None
        self.list_objs = None

    def test_id_default(self):
        """Test default id."""
        bs = Base()
        self.assertEqual(bs.id, 2)

    def test_id_no_arguments_passed(self):
        """Test id with no arguments passed."""
        bs1 = Base()
        bs2 = Base()
        bs3 = Base()
        self.assertEqual(bs1.id, 2)
        self.assertEqual(bs2.id, 3)
        self.assertEqual(bs3.id, 4)

    def test_id_passing_argument(self):
        """Test passing one argument as id"""
        bs = Base(10)
        self.assertEqual(bs.id, 10)

    def test_id_passing_different_arguments(self):
        """Test passing different types of arguments as id."""
        bs1 = Base(None)
        bs2 = Base(0.5)
        bs3 = Base('Hello')
        bs4 = Base([None, 0.5, 'Hello'])
        self.assertEqual(bs1.id, 2)
        self.assertEqual(bs2.id, 0.5)
        self.assertEqual(bs3.id, "Hello")
        self.assertEqual(bs4.id, [None, 0.5, 'Hello'])

    def test_initialize_with_two_args(self):
        """Test passing more args to Base"""
        with self.assertRaises(TypeError):
            bs = Base(1, 5)

    def test_accessing_private_attribute(self):
        """Test accessing the private attribute."""
        bs = Base()
        with self.assertRaises(AttributeError):
            bs.__nb_objects

    def test_to_json_string(self):
        """Test the to_json_string method of the Base class."""
        expected_output = '[]'
        result = Base.to_json_string([])
        self.assertEqual(result, expected_output)

        expected_output = '[{"id": 1}]'
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, expected_output)

    def test_save_to_file(self):
        """Test the save_to_file method of the Base class."""
        with self.assertRaises(AttributeError):
            Base.save_to_file(self.list_objs)

    def test_from_json_string(self):
        """Test the from_json_string method of the Base class."""
        expected_output = []
        result = Base.from_json_string('')
        self.assertEqual(result, expected_output)

        expected_output = [{"id": 1}]
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, expected_output)

    def test_create(self):
        """Test the create method of the Base class."""
        with self.assertRaises(UnboundLocalError):
            Base.create(id=1)
