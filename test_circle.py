"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class CircleTest(unittest.TestCase):
    def test_add_area_typical(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = c1.add_area(c2)
        # Checking radius
        self.assertAlmostEquals(4.47213595499958, c3.get_radius(), places=5)

        # Checking area
        self.assertAlmostEquals(62.83185307179588, c3.get_area(), places=5)

    def test_add_area_edge(self):
        c1 = Circle(0)
        c2 = Circle(6)
        c3 = c2.add_area(c1)
        # Checking radius
        self.assertEqual(c2.get_radius(), c3.get_radius())

        # Checking area
        self.assertEqual(c2.get_area(), c3.get_area())

    def test_radius_negative(self):
        with self.assertRaises(ValueError):
            Circle(-2)

