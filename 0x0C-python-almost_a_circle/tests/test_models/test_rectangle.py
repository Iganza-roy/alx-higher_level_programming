#!/usr/bin/python3
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):

    def test_attributes(self):
        rect = Rectangle(4, 6, 2, 3, 1)

        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_validators(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 6, 2, 3, 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 6, 2, 3, 1)

        with self.assertRaises(TypeError):
            Rectangle(4, "invalid", 2, 3, 1)

        with self.assertRaises(ValueError):
            Rectangle(4, -6, 2, 3, 1)

        with self.assertRaises(TypeError):
            Rectangle(4, 6, "invalid", 3, 1)

        with self.assertRaises(ValueError):
            Rectangle(4, 6, -2, 3, 1)

        with self.assertRaises(TypeError):
            Rectangle(4, 6, 2, "invalid", 1)

        with self.assertRaises(ValueError):
            Rectangle(4, 6, 2, -3, 1)

    def test_area(self):
        rect = Rectangle(4, 6, 2, 3, 1)

        self.assertEqual(rect.area(), 24)

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_display(self):
        r = Rectangle(3, 4, 1, 2)

        with StringIO() as buffer:
            sys.stdout = buffer
            r.display()
            captured_output = buffer.getvalue()

        expected_output = ' ###\n ###\n ###\n ###\n'
        self.assertEqual(captured_output, expected_output)

    def test_str(self):
        rect = Rectangle(4, 6, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 4/6")

    def test_update(self):
        rect = Rectangle(4, 6, 2, 3, 1)

        rect.update(2, 8, 10, 4, 5)

        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.update(width=12, y=7)

        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.y, 7)


if __name__ == '__main__':
    unittest.main()
