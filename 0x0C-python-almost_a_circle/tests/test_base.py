#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    def test_base_creation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_creation_with_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_base_creation_after_id(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_base_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_create_method(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_save_and_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8, 6)
        json_str = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(str, type(json_str))


if __name__ == '__main__':
    unittest.main()
