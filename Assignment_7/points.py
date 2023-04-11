import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.a = Point(0, 0)
        self.b = Point(10, 5)
        self.c = Point(5, 10)
        self.d = Point(2, 8)
        self.e = Point(-3, -9)
        self.f = Point(-2, 5)

    def test_str(self):
        self.assertEqual(str(self.a), "(0, 0)")
        self.assertEqual(str(self.c), "(5, 10)")

    def test_repr(self):
        self.assertEqual(repr(self.b), "Point(10, 5)")
        self.assertEqual(repr(self.d), "Point(2, 8)")

    def test_eq(self):
        self.assertTrue(self.a == Point(0, 0))
        self.assertFalse(self.b == self.e)

    def test_ne(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.d != Point(2, 8))

    def test_add(self):
        self.assertEqual(self.a + self.f, Point(-2, 5))
        self.assertEqual(self.b + self.e, Point(7, -4))

    def test_sub(self):
        self.assertEqual(self.e - self.a, Point(-3, -9))
        self.assertEqual(self.b - self.f, Point(12, 0))

    def test_mul(self):
        self.assertEqual(self.b * self.f, 5)
        self.assertEqual(self.c * self.e, -105)

    def test_cross(self):
        self.assertEqual(self.b.cross(self.f), 60)
        self.assertEqual(self.c.cross(self.e), -15)

    def test_length(self):
        self.assertEqual(self.b.length(), math.sqrt(125))
        self.assertEqual(self.a.length(), 0)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
