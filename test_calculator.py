import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-2, 4), 2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(-1, -4), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)
        self.assertEqual(self.calc.multiply(2, -4), -8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, -4), -2)
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 2), 1)
        self.assertEqual(self.calc.modulo(3, 5), 3)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()