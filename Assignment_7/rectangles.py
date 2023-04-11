from points import Point


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

    @classmethod
    def from_points(cls, p):
        if not isinstance(p, (list, tuple)):
            raise ValueError("It is neither a list nor a tuple")
        if len(p) != 2:
            raise ValueError("These are not 2 points!")
        if not (isinstance(p[0], Point) and isinstance(p[1], Point)):
            raise ValueError("At least 1 value is not a point!")
        return Rectangle(p[0].x, p[0].y, p[1].x, p[1].y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
