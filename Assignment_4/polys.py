import unittest


def add_poly(poly1, poly2):  # poly1(x) + poly2(x)
    maxl = max(len(poly1), len(poly2))
    poly1 += [0] * (maxl - len(poly1))
    poly2 += [0] * (maxl - len(poly2))
    poly3 = [poly1[i] + poly2[i] for i in range(len(poly1))]
    return poly3


def sub_poly(poly1, poly2):  # poly1(x) - poly2(x)
    maxl = max(len(poly1), len(poly2))
    poly1 += [0] * (maxl - len(poly1))
    poly2 += [0] * (maxl - len(poly2))
    poly3 = [poly1[i] - poly2[i] for i in range(len(poly1))]
    return poly3


def mul_poly(poly1, poly2):  # poly1(x) * poly2(x)
    poly3 = [0 for _ in range(len(poly1) + len(poly2) - 1)]
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            poly3[i + j] += poly1[i] * poly2[j]
    return poly3


def is_zero(poly):  # bool, [0], [0,0], itp.
    for i in poly:
        if i != 0:
            return False
    return True


def eq_poly(poly1, poly2):  # bool, porównywanie poly1(x) == poly2(x)
    if len(poly1) != len(poly2):
        return False
    for i in range(len(poly1)):
        if poly1[i] != poly2[i]:
            return False
    return True


def eval_poly(poly, x0):  # poly(x0), algorytm Hornera
    result = poly[-1]
    for i in range(len(poly) - 2, -1, -1):
        result = result * x0 + poly[i]
    return result


def combine_poly(poly1, poly2):  # poly1(poly2(x)), trudne!
    poly3 = [0 for _ in range((len(poly1) - 1) * (len(poly2) - 1) + 1)]
    for i in range(len(poly1)):
        for count, j in enumerate(mul_poly([poly1[i]], pow_poly(poly2, i))):
            poly3[count] += j
    return poly3


def pow_poly(poly, n):  # poly(x) ** n
    if n == 0:
        return [1]
    poly1 = poly.copy()
    for i in range(n - 1):
        poly1 = mul_poly(poly1, poly)
    return poly1


def diff_poly(poly):  # pochodna wielomianu
    poly1 = []
    for i in range(1, len(poly)):
        poly1.append(i * poly[i])
    return poly1

# p1 = [2, 1]      # W(x) = 2 + x
# p2 = [2, 1, 0]   # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]  # W(x) = -3 + x^2
# p4 = [3]         # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]         # zero
# p6 = [0, 0, 0]   # zero (niejednoznaczność)


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]           # W(x) = x
        self.p2 = [0, 0, 1]        # W(x) = x^2
        self.p3 = [1, 1, 1, 1]
        self.p4 = [-1, 4, -5, 2]
        self.p5 = [-15, 5, -3, 1]
        self.x01 = 1
        self.x02 = 3
        self.n = 3

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p2, self.p3), [1, 1, 2, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        self.assertEqual(mul_poly(self.p2, self.p3), [0, 0, 1, 1, 1, 1])

    def test_is_zero(self):
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero(self.p2))

    def test_eq_poly(self):
        self.assertFalse(eq_poly(self.p1, self.p2))
        self.assertTrue(self.p1, self.p1)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p4, self.x01), 0)
        self.assertEqual(eval_poly(self.p5, self.x02), 0)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p3, self.p4), [0, 8, -42, 148, -322, 436, -373, 198, -60, 8])
        self.assertEqual(combine_poly(self.p4, self.p5), [-7936, 7520, -6887, 4604, -2255, 990, -329, 84, -18, 2])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, self.n), [0, 0, 0, 1])
        self.assertEqual(pow_poly(self.p2, self.n), [0, 0, 0, 0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p2), [0, 2])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
