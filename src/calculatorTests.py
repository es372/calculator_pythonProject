import unittest
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        system = Calculator()
        self.assertIsInstance(system, Calculator)

    def test_addMethod(self):
        self.assertEqual(self.Calculator.add(2, 2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_subtractMethod(self):
        self.assertEqual(self.Calculator.subtract(2, 2), 0)
        self.assertEqual(self.Calculator.result, 0)

    def test_multiplyMethod(self):
        self.assertEqual(self.Calculator.multiply(2, 2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_divisionMethod(self):
        self.assertEqual(self.Calculator.divide(2, 2), 1)
        self.assertEqual(self.Calculator.result, 1)

    def test_squareMethod(self):
        self.assertEqual(self.Calculator.square(2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_squareRootMethod(self):
        self.assertEqual(self.Calculator.sqrt(4), 2)
        self.assertEqual(self.Calculator.result, 2)




if __name__ == '__main__':
    unittest.main()