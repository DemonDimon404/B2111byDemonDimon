import unittest
from main import *

class MyTest(unittest.TestCase):
    def test_arg(self):
        self.assertEqual(adder(2,2), 4)
    def test_kwarg(self):
        self.assertEqual(adder(a=10,b=11), 21)
    def test_mixed(self):
        self.assertEqual(adder(1,c=45), 46)
    def test_dif(self):
        x = 10
        y = 5
        self.assertEqual(adder(0, -5),y, a=x)
    def test_wrong_type(self):
        self.assertEqual(adder("5","abc", 10), 15)

if __name__ == '__main__':
    unittest.main()
