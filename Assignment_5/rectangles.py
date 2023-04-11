from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self


# Kod testujący moduł.


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(0, 0, 5, 5)
        self.b = Rectangle(1, 2, 3, 4)
        self.c = Rectangle(-3, -4, -1, -2)
        self.d = Rectangle(1, 1, 6, 6)

    def test_str(self):
        self.assertEqual(str(self.a), "[(0, 0), (5, 5)]")
        self.assertEqual(str(self.c), "[(-3, -4), (-1, -2)]")

    def test_repr(self):
        self.assertEqual(repr(self.b), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.d), "Rectangle(1, 1, 6, 6)")

    def test_eq(self):
        self.assertTrue(self.a == Rectangle(0, 0, 5, 5))
        self.assertFalse(self.b == self.c)

    def test_ne(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.d != Rectangle(1, 1, 6, 6))

    def test_center(self):
        self.assertEqual(self.b.center(), Point(2, 3))
        self.assertEqual(self.d.center(), Point(3.5, 3.5))

    def test_area(self):
        self.assertEqual(self.a.area(), 25)
        self.assertEqual(self.c.area(), 4)

    def test_move(self):
        self.assertEqual(self.c.move(5, -5), Rectangle(2, -9, 4, -7))
        self.assertEqual(self.b.move(-3, 0), Rectangle(-2, 2, 0, 4))


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
