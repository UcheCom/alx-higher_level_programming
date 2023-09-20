#!/usr/bin/python3
"""Class test cases for square methods"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestSquareMethods(unittest.TestCase):
    """Test cases for Square class methods"""

    def setUp(self):
        """setUp method"""
        Base._Base__nb_objects = 0

    def test_square_1_arg(self):
        """Test init method with one arg"""
        s = Square(3)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_args(self):
        """Test init method with all args"""
        s = Square(1, 2, 3, 8)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 8)

    def test_squares(self):
        """Test 2 squares"""
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(False, s1 is s2)
        self.assertEqual(False, s1.id == s2.id)

    def test_is_Rect_instance(self):
        """Test square is a Rectangle instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Rectangle))

    def test_is_Base_instance(self):
        """Test square is a Base instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Base))

    def test_0_arg(self):
        """Test with 0 args"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_5_args(self):
        """Test with 5 args"""
        with self.assertRaises(TypeError):
            s = Square(2, 2, 2, 2, 2)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_access_width(self):
        """Test accessing width"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_height(self):
        """Test accessing height"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_x(self):
        """Test accessing x"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_y(self):
        """Test accessing y"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y

    def test_valid_size(self):
        """Test size string"""
        with self.assertRaises(TypeError):
            s = Square("1", 1, 2, 2)

    def test_valid_x(self):
        """Test x string"""
        with self.assertRaises(TypeError):
            s = Square(1, '1', 1, 1)

    def test_valid_y(self):
        """Test y string"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, '1', 1)

    def test_size_0(self):
        """Test case of a size 0"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_neg(self):
        """Test case for x negative"""
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """Test case for y negative"""
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_size_neg(self):
        """Test case os negative size"""
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_area(self):
        """Test the return value of the area method"""
        s = Square(3)
        self.assertEqual(s.area(),9)

    def test_area_size(self):
        """Test area and update size"""
        s = Square(4)
        self.assertEqual(s.area(), 16)
        s.size = 6
        self.assertEqual(s.area(), 36)

    def test_display(self):
        """Test printed string"""
        s = Square(2)
        rest = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_display_size(self):
        """Test printed string and modified size"""
        s = Square(2)
        rest = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

        s.size = 3
        rest = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_dislay_xy(self):
        """Test string printed with x and y"""
        s = Square(2)
        rest = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

        s.x = 1
        rest = " ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

        s.y = 2
        rest = "\n\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), rest)

    def test_str(self):
        """Test the __str___ return value"""
        s = Square(2)
        rest = "[Square] (1) 0/0 - 2"
        self.assertEqual(s.__str__(), rest)

    def test_str_2(self):
        """Test __str__ return value"""
        s = Square(5, 3, 3)
        rest = "[Square] (1) 3/3 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

    def test_str_3(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2, 2)
        rest = "[Square] (2) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s.id = 2
        s.size = 11
        rest = "[Square] (2) 2/2 - 11\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

    def test_str_4(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2)
        rest = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s2 = Square(2)
        rest = "[Square] (2) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s2)
            self.assertEqual(std_out.getvalue(), rest)

        s3 = Square(1, 1, 1)
        rest = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s3)
            self.assertEqual(std_out.getvalue(), rest)

    def test_update(self):
        """Test update method"""
        s = Square(2)
        rest = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s.update(2)
        rest = "[Square] (2) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

    def test_update_2(self):
        """Test update method"""
        s = Square(2)
        rest = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s.update(4, 2, 2, 2)
        rest = "[Square] (4) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s.update(y=5)
        rest = "[Square] (4) 2/5 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        s.update(id=11, size=6)
        rest = "[Square] (11) 2/5 - 6\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

    def test_udpate_3(self):
        """Test update method"""
        s = Square(5)
        rest = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        dictn = {'size': 5, 'y': 6}
        s.update(**dictn)
        rest = "[Square] (1) 0/6 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

    def test_update_4(self):
        """Test udpate method"""
        s = Square(5)
        rest = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        dictn = {'id': 11, 'x': '6', 'y': 2}
        with self.assertRaises(TypeError):
            s.update(**dictn)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        s = Square(1, 3, 5)
        rest = "[Square] (1) 3/5 - 1\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), rest)

        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)
        self.assertEqual(s.id, 1)

        rest = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(type(s.to_dictionary()))
            self.assertEqual(std_out.getvalue(), rest)

    def test_create_one(self):
        dictionary = {'id': 99}
        s = Square.create(**dictionary)
        self.assertEqual(s.id, 99)

    def test_create_two(self):
        dictionary = {'id': 99, 'size': 4}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 4)

    def test_create_three(self):
        dictionary = {'id': 99, 'size': 3, 'x': 5}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 5)

    def test_create_four(self):
        dictionary = {'id': 99, 'size': 2, 'x': 3, 'y': 4}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_save_to_file(self):
        """Test save to file"""
        Square.save_to_file([Square(1)])
        rest = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json", "r") as a:
            self.assertEqual(a.read(), rest)

if __name__ == "__main__":
    unittest.main()
