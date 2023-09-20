#!/usr/bin/python3
"""This is package model for test cases"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestBase_Methods(unittest.TestCase):
    """Unittest cases for Base class methods"""

    def setUp(self):
        """SetUp test method"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """Test the default id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id(self):
        """Test the id with int"""
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_multiple_id(self):
        """test id with multiple class instance"""
        b = Base()
        b2 = Base()
        b3 = Base(99)
        b4 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 99)
        self.assertEqual(b4.id, 3)

    def test_string_id(self):
        """ Test string id"""
        b = Base("1")
        self.assertEqual(b.id, "1")

    def test_two_args_id(self):
        """Test 2 args id for init method"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_private_attr(self):
        """Testing the private attr"""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

    def test_to_json_string(self):
        """ Test Dictionary to JSON string """
        b = Rectangle(3, 3)
        dictionary = b.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        b = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(json_dictionary)
            self.assertEqual(std_out.getvalue(), b.replace("'", "\""))

    def test_save_to_file(self):
        """ Test save to file """
        Square.save_to_file(None)
        b = "[]"
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), b)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test save to file """
        Rectangle.save_to_file(None)
        b = "[]"
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), b)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 99}
        b = Rectangle.create(**dictionary)
        self.assertEqual(b.id, 99)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 99, 'width': 2}
        b = Rectangle.create(**dictionary)
        self.assertEqual(b.id, 99)
        self.assertEqual(b.width, 2)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 99, 'width': 2, 'height': 3}
        b = Rectangle.create(**dictionary)
        self.assertEqual(b.id, 99)
        self.assertEqual(b.width, 2)
        self.assertEqual(b.height, 3)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 99, 'width': 2, 'height': 3, 'x': 4}
        b = Rectangle.create(**dictionary)
        self.assertEqual(b.id, 99)
        self.assertEqual(b.width, 2)
        self.assertEqual(b.height, 3)
        self.assertEqual(b.x, 4)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 99, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        b = Rectangle.create(**dictionary)
        self.assertEqual(b.id, 99)
        self.assertEqual(b.width, 2)
        self.assertEqual(b.height, 3)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 5)
