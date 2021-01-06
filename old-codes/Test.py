import unittest
import math
from digit import validate_pin


class FirstTest (unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(math.floor(3.50), 3)

    def test2(self):
        self.assertFalse(validate_pin("123a"))

if __name__=='__main__':
    unittest.main()
