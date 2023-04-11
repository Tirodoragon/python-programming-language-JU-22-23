from rectangles import Rectangle
from points import Point
import pytest


class TestRectangles:
    @pytest.fixture(scope="class")
    def rectangleA(self):
        return Rectangle(0, 0, 5, 5)

    @pytest.fixture(scope="class")
    def rectangleB(self):
        return Rectangle(1, 2, 3, 4)

    @pytest.fixture(scope="class")
    def rectangleC(self):
        return Rectangle(-3, -4, -1, -2)

    @pytest.fixture(scope="class")
    def rectangleD(self):
        return Rectangle(1, 1, 6, 6)

    @pytest.fixture(scope="class")
    def rectangleE(self):
        return Rectangle(5, 6, 7, 8)

    def test_init(self):
        pytest.raises(ValueError, Rectangle, 2, 0, 1, 0)
        pytest.raises(ValueError, Rectangle, 5, 3, 5, 2)

    def test_str(self, rectangleA, rectangleC):
        assert str(rectangleA) == "[(0, 0), (5, 5)]"
        assert str(rectangleC) == "[(-3, -4), (-1, -2)]"

    def test_repr(self, rectangleB, rectangleD):
        assert repr(rectangleB) == "Rectangle(1, 2, 3, 4)"
        assert repr(rectangleD) == "Rectangle(1, 1, 6, 6)"

    def test_eq(self, rectangleA, rectangleB, rectangleC):
        assert rectangleA == Rectangle(0, 0, 5, 5)
        assert not rectangleB == rectangleC
        pytest.raises(ValueError, rectangleC.__eq__, (0, 1))

    def test_ne(self, rectangleA, rectangleB, rectangleD, rectangleC):
        assert rectangleA != rectangleB
        assert not rectangleD != Rectangle(1, 1, 6, 6)
        pytest.raises(ValueError, lambda: rectangleC == "tak")

    def test_center(self, rectangleB, rectangleD):
        assert rectangleB.center() == Point(2, 3)
        assert rectangleD.center() == Point(3.5, 3.5)

    def test_area(self, rectangleA, rectangleC):
        assert rectangleA.area() == 25
        assert rectangleC.area() == 4

    def test_intersection(self, rectangleA, rectangleB, rectangleC, rectangleD):
        assert rectangleA.intersection(rectangleB) == Rectangle(1, 2, 3, 4)
        pytest.raises(ValueError, rectangleC.intersection, rectangleD)
        pytest.raises(ValueError, rectangleC.intersection, 'd')

    def test_cover(self, rectangleA, rectangleB, rectangleD, rectangleC):
        assert rectangleA.cover(rectangleB) == Rectangle(0, 0, 5, 5)
        assert rectangleC.cover(rectangleD) == Rectangle(-3, -4, 6, 6)
        pytest.raises(ValueError, lambda: rectangleC.cover([1, 0]))

    def test_make4(self, rectangleB, rectangleD):
        assert rectangleB.make4() == (Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4),
                                      Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3))
        assert rectangleD.make4() == (Rectangle(1, 3.5, 3.5, 6), Rectangle(3.5, 3.5, 6, 6),
                                      Rectangle(1, 1, 3.5, 3.5), Rectangle(3.5, 1, 6, 3.5))

    def test_from_points(self, rectangleE):
        assert Rectangle.from_points((Point(5, 6), Point(7, 8))) == rectangleE
        pytest.raises(ValueError, lambda: Rectangle.from_points(1))
        pytest.raises(ValueError, lambda: Rectangle.from_points(Point(1, 2)))
        pytest.raises(ValueError, lambda: Rectangle.from_points((Point(3, 4), 5)))

    def test_top(self, rectangleC, rectangleE):
        assert rectangleC.top == -2
        assert rectangleE.top == 8

    def test_left(self, rectangleC, rectangleE):
        assert rectangleC.left == -3
        assert rectangleE.left == 5

    def test_bottom(self, rectangleC, rectangleE):
        assert rectangleC.bottom == -4
        assert rectangleE.bottom == 6

    def test_right(self, rectangleC, rectangleE):
        assert rectangleC.right == -1
        assert rectangleE.right == 7

    def test_width(self, rectangleC, rectangleE):
        assert rectangleC.width == 2
        assert rectangleE.width == 2

    def test_height(self, rectangleC, rectangleE):
        assert rectangleC.height == 2
        assert rectangleE.height == 2

    def test_topleft(self, rectangleC, rectangleE):
        assert rectangleC.topleft == Point(-3, -2)
        assert rectangleE.topleft == Point(5, 8)

    def test_bottomleft(self, rectangleC, rectangleE):
        assert rectangleC.bottomleft == Point(-3, -4)
        assert rectangleE.bottomleft == Point(5, 6)

    def test_topright(self, rectangleC, rectangleE):
        assert rectangleC.topright == Point(-1, -2)
        assert rectangleE.topright == Point(7, 8)

    def test_bottomright(self, rectangleC, rectangleE):
        assert rectangleC.bottomright == Point(-1, -4)
        assert rectangleE.bottomright == Point(7, 6)

    def test_move(self, rectangleC, rectangleB, rectangleA):
        assert rectangleC.move(5, -5) == Rectangle(2, -9, 4, -7)
        assert rectangleB.move(-3, 0) == Rectangle(-2, 2, 0, 4)
        pytest.raises(ValueError, rectangleA.move, "tak", "nie")

if __name__ == "__main__":
    pytest.main()
