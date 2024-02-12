#!/usr/bin/python3

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def setUp(self):
        self.square_with_args = Square(10, 2, 1, 1)
        self.square_without_args = Square(1, 2, 10)

    def test_is_base(self):
        self.assertIsInstance(self.square_with_args, Base)
        self.assertIsInstance(self.square_without_args, Base)

    def test_is_rectangle(self):
        self.assertIsInstance(self.square_with_args, Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()
        invalid_sizes = [None, "invalid", 5.5, complex(5), {
            "a": 1, "b": 2
            }, True, [1, 2, 3]]
        for size in invalid_sizes:
            with self.subTest(size=size):
                with self.assertRaisesRegex(
                        TypeError, "width must be an integer"
                        ):
                    Square(size)

    def test_negative_and_zero_size(self):
        invalid_sizes = [-1, 0]
        for size in invalid_sizes:
            with self.subTest(size=size):
                with self.assertRaisesRegex(ValueError, "width must be > 0"):
                    Square(size, 2)

    def test_invalid_value_for_x_and_y(self):
        invalid_values = [None, "invalid", 5.5, complex(5), {
            "a": 1, "b": 2
            }, True, [1, 2, 3]]
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Square(1, value, 0)

                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Square(1, 0, value)
