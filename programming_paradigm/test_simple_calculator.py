import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 2), 12)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main":
    unittest.main()
