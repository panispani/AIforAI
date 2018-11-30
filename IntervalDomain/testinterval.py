from interval import *
import unittest

class TestInterval(unittest.TestCase):

    def test_relu(self):
        print("Test Interval relu")
        self.assertEqual((1, 1), relu((1, 1)))
        self.assertEqual((0, 0), relu((0, 0)))
        self.assertEqual((0, 0), relu((-4, -1)))
        self.assertEqual((0, 2), relu((-4, 2)))
        self.assertEqual((10, 11), relu((10, 11)))

if __name__ == '__main__':
    unittest.main()
