import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)          # positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # negative + positive
        self.assertEqual(self.calc.add(-2, -3), -5)       # negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)          # zeros

    # ---------- Subtraction Tests ----------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)     # normal case
        self.assertEqual(self.calc.subtract(3, 5), -2)    # result negative
        self.assertEqual(self.calc.subtract(-3, -2), -1)  # negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)     # zeros

    # ---------- Multiplication Tests ----------
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)     # positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)   # negative * positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)   # negative * negative
        self.assertEqual(self.calc.multiply(0, 5), 0)     # multiply by zero

    # ---------- Division Tests ----------
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)      # normal division
        self.assertEqual(self.calc.divide(-10, 2), -5)    # negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5)    # negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5)    # both negative
        self.assertIsNone(self.calc.divide(5, 0))         # division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)       # zero numerator

if __name__ == "__main__":
    unittest.main()
