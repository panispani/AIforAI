from interval import *
import unittest

class TestInterval(unittest.TestCase):

    def test_relu_number(self):
        print("\nTest relu of a single number")
        self.assertEqual(0, relu_number(-5))
        self.assertEqual(0, relu_number(0))
        self.assertEqual(3, relu_number(3))
        print("PASSED")

    def test_relu(self):
        print("\nTest Interval relu")
        self.assertEqual((1, 1), relu((1, 1)))
        self.assertEqual((0, 0), relu((0, 0)))
        self.assertEqual((0, 0), relu((-4, -1)))
        self.assertEqual((0, 2), relu((-4, 2)))
        self.assertEqual((10, 11), relu((10, 11)))
        print("PASSED")

    def test_add(self):
        print("\nTest Interval addition")
        self.assertEqual((2, 4), add((0, 1), (2, 3)))
        self.assertEqual((1, 4), add((-1, 1), (2, 3)))
        print("PASSED")

    def test_sub(self):
        print("\nTest Interval substraction")
        self.assertEqual((-3, -1), sub((0, 1), (2, 3)))
        self.assertEqual((-4, -1), sub((-1, 1), (2, 3)))
        self.assertEqual((-7, -4), sub((-4, -2), (2, 3)))
        self.assertEqual((4, 7), sub((1, 2), (-5, -3)))
        self.assertEqual((2, 7), sub((-1, 2), (-5, -3)))
        self.assertEqual((-4, 7), sub((-1, 2), (-5, 3)))
        self.assertEqual((-2, 7), sub((1, 2), (-5, 3)))
        print("PASSED")

    def test_mul_constant(self):
        print("\nTest Interval multiplication by constant")
        self.assertEqual((2, 4), mul_constant((1, 2), 2))
        self.assertEqual((-4, -2), mul_constant((1, 2), -2))
        self.assertEqual((0, 0), mul_constant((1, 2), 0))
        print("PASSED")

    def test_to_interval(self):
        print("\nTest conversion of number to Interval")
        self.assertEqual((2, 2), to_interval(2))
        self.assertEqual((-1, -1), to_interval(-1))
        self.assertEqual((0, 0), to_interval(0))
        print("PASSED")

if __name__ == '__main__':
    unittest.main()
