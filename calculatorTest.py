import unittest
from calculator import *

class calculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertTrue(add(2, 5) == 7)

if __name__ == '__main__':
    unittest.main()