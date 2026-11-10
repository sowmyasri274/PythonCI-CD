
from arth import *
import unittest

class TestArth(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 9), 14)

    def test_sub(self):
        self.assertEqual(sub(8, 2), 6)

    def test_mul(self):
        self.assertEqual(mul(5, 2), 10)

if __name__ == "__main__":
    unittest.main()
