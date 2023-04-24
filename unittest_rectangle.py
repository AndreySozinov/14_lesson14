import unittest
from Rectangle import Rectangle


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(5, 2)

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 14)

    def test_area(self):
        self.assertEqual(self.r1.area(), 10)

    def test_add(self):
        self.assertEqual(self.r1 + self.r1, Rectangle(7))

    def test_sub(self):
        self.assertEqual(self.r1 - Rectangle(4, 1), Rectangle(1))


if __name__ == '__main__':
    unittest.main()
