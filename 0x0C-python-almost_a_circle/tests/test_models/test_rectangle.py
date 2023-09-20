#!/usr/bin/python3
"""This is the test use cases for rectangle class methods"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangle_Methdods(unittest.TestCase):
    """Test cases for rectangke class methods"""

    def setUp(self):
        """setUp method"""
        Base._Base__nb_objects = 0

    def test_new_rec(self):
        """This tests a new rectangle"""
        r = Rectangle(1, 1, 1, 1, 99)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 99)

    def test_new_rec_two(self):
        """This tests new rectangle with missing default attributes"""
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_2_rectangles(self):
        """This tests 2 new rectangles"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(False, r1 is r2)
        self.assertEqual(False, r1.id == r2.id)

    def test_is_Base_instance(self):
        """Test if a rectangle is a Base class instance"""
        r = Rectangle(1, 1)
        self.assertEqual(True, isinstance(r, Base))

    def test_arg_one(self):
        """This tests init method with 1 arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_arg_zero(self):
        """This tests init method with 0 arg"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_check_value(self):
        """ This test args passed """
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 3)

    def test_check_value_two(self):
        """ This test args passed """
        with self.assertRaises(ValueError):
            r = Rectangle(2, -3)

    def test_access_width(self):
        """Accessing width"""
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width

    def test_access_height(self):
        """Accessing height"""
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__height

    def test_access_x(self):
        """Accessing x"""
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__x

    def test_access_y(self):
        """ Accessing y"""
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__y

    def test_width_string_attr(self):
        """Tests init method with a string attribute width"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1)

    def test_height_string_attr(self):
        """Tests init method with a string attrubute height"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, "1")

    def test_x_string_attr(self):
        """Tests init method with a string attribute x"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, "1", 1, 1)

    def test_y_string_attr(self):
        """Tests init method with a string attribute y"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, "1", 1)

    def test_width_0(self):
        """Tests init method with a width = 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_height_0(self):
        """"Tests init method with a height = 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_x_neg(self):
        """Tests init mehtod with negative x"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -1)

    def test_y_neg(self):
        """Tests init method with negative y"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Tests the value of the area of a rectangle"""
        r = Rectangle(4, 11)
        self.assertEqual(r.area(), 44)

    def test_area_change(self):
        """Tests the area of a rectangle with modified attrs"""
        r = Rectangle(4, 9)
        self.assertEqual(r.area(), 36)
        r.width = 5
        self.assertEqual(r.area(), 45)
        r.height = 3
        self.assertEqual(r.area(), 15)

    def test_area_two_rec(self):
        """Tests the area of 2 rectangles"""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(6, 4)
        self.assertEqual(r1.area(), 15)
        self.assertEqual(r2.area(), 24)

    def test_display(self):
        """Tests the printed string"""
        r = Rectangle(2, 4)
        rest = "##\n" + "##\n" + "##\n" + "##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_display_change(self):
        """Tests the printed string with modified width and height"""
        r = Rectangle(1, 3)
        rest = "#\n" + "#\n" + "#\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

        r.width = 2
        rest = "##\n" + "##\n" + "##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_display_change(self):
        """Tests display with x and y to default"""
        r = Rectangle(1, 2, 1, 1)
        rest = "\n #\n #\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_display_change(self):
        """ Test display with x and y modified"""
        r = Rectangle(2, 4)
        rest = "##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

        r.x = 2
        rest = "  ##\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

        r.y = 1
        rest = "\n  ##\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            r.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_to_dictionary_output(self):
        r = Rectangle(12, 3, 4, 5, 8)
        Uchenna = {'x': 4, 'y': 5, 'id': 8, 'height': 3, 'width': 12}
        self.assertDictEqual(Uchenna, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(12, 3, 4, 5, 8)
        r2 = Rectangle(8, 5, 4, 3, 12)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(13, 3, 5, 1, 3)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

    def test_save_to_file(self):
        """Test save to file"""
        Rectangle.save_to_file([Rectangle(1, 3)])
        rest = '[{"id": 1, "width": 1, "height": 3, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as t:
            self.assertEqual(t.read(), rest)

if __name__ == "__main__":
    unittest.main()
