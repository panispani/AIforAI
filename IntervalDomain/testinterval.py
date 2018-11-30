from interval import *
import unittest

class TestInterval(unittest.TestCase):

    def test_relu(self):
        print("\nTest Interval relu")
        self.assertEqual((1, 1), relu((1, 1)))
        self.assertEqual((0, 0), relu((0, 0)))
        self.assertEqual((0, 0), relu((-4, -1)))
        self.assertEqual((0, 2), relu((-4, 2)))
        self.assertEqual((10, 11), relu((10, 11)))
        print("PASSED")

    def test_relu_number(self):
        print("\nTest relu of a single number")
        self.assertEqual(0, relu_number(-5))
        self.assertEqual(0, relu_number(0))
        self.assertEqual(3, relu_number(3))
        print("PASSED")

    def test_addition(self):
        print("\nTest Interval addition")
        self.assertEqual((2, 4), addition((0, 1), (2, 3)))
        self.assertEqual((1, 4), addition((-1, 1), (2, 3)))
        print("PASSED")

if __name__ == '__main__':
    unittest.main()
