from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 and y1 >= y2:
            raise ValueError("Invalid points!")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):  # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            raise ValueError("It is not a rectangle!")

        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        if not isinstance(other, Rectangle):
            raise ValueError("It is not a rectangle!")

        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("It is not a number!")

        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("It is not a rectangle!")

        x1 = max(self.pt1.x, other.pt1.x)
        x2 = min(self.pt2.x, other.pt2.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 > x2 or y1 > y2:
            raise ValueError("There is no intersection!")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):  # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("It is not a rectangle!")

        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = min(self.pt1.y, other.pt1.y)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):  # zwraca krotkę czterech mniejszych
        cntr = self.center()
        rec1 = Rectangle(self.pt1.x, cntr.y, cntr.x, self.pt2.y)
        rec2 = Rectangle(cntr.x, cntr.y, self.pt2.x, self.pt2.y)
        rec3 = Rectangle(self.pt1.x, self.pt1.y, cntr.x, cntr.y)
        rec4 = Rectangle(cntr.x, self.pt1.y, self.pt2.x, cntr.y)
        return rec1, rec2, rec3, rec4

# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C


# Kod testujący moduł.

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(0, 0, 5, 5)
        self.b = Rectangle(1, 2, 3, 4)
        self.c = Rectangle(-3, -4, -1, -2)
        self.d = Rectangle(1, 1, 6, 6)
        self.assertRaises(ValueError, Rectangle, 2, 0, 1, 0)
        self.assertRaises(ValueError, Rectangle, 5, 3, 5, 2)

    def test_str(self):
        self.assertEqual(str(self.a), "[(0, 0), (5, 5)]")
        self.assertEqual(str(self.c), "[(-3, -4), (-1, -2)]")

    def test_repr(self):
        self.assertEqual(repr(self.b), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.d), "Rectangle(1, 1, 6, 6)")

    def test_eq(self):
        self.assertTrue(self.a == Rectangle(0, 0, 5, 5))
        self.assertFalse(self.b == self.c)
        self.assertRaises(ValueError, self.c.__eq__, (0, 1))

    def test_ne(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.d != Rectangle(1, 1, 6, 6))
        self.assertRaises(ValueError, lambda: self.c == "tak")

    def test_center(self):
        self.assertEqual(self.b.center(), Point(2, 3))
        self.assertEqual(self.d.center(), Point(3.5, 3.5))

    def test_area(self):
        self.assertEqual(self.a.area(), 25)
        self.assertEqual(self.c.area(), 4)

    def test_move(self):
        self.assertEqual(self.c.move(5, -5), Rectangle(2, -9, 4, -7))
        self.assertEqual(self.b.move(-3, 0), Rectangle(-2, 2, 0, 4))
        self.assertRaises(ValueError, self.a.move, "tak", "nie")

    def test_intersection(self):
        self.assertEqual(self.a.intersection(self.b), Rectangle(1, 2, 3, 4))
        self.assertRaises(ValueError, self.c.intersection, self.d)
        self.assertRaises(ValueError, self.c.__eq__, 'd')

    def test_cover(self):
        self.assertEqual(self.a.cover(self.b), Rectangle(0, 0, 5, 5))
        self.assertEqual(self.c.cover(self.d), Rectangle(-3, -4, 6, 6))
        self.assertRaises(ValueError, lambda: self.c == [1, 0])

    def test_make4(self):
        self.assertEqual(self.b.make4(), (Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4),
                                          Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3)))
        self.assertEqual(self.d.make4(), (Rectangle(1, 3.5, 3.5, 6), Rectangle(3.5, 3.5, 6, 6),
                                          Rectangle(1, 1, 3.5, 3.5), Rectangle(3.5, 1, 6, 3.5)))


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
