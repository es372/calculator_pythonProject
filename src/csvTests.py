import unittest
from csvReader import CsvReader
from calculator import Calculator
from pprint import pprint

class CalculatorCsvTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_csvReader_addition(self):
        self.csv_reader = CsvReader('./src/addition.csv')
        for values in self.csv_reader.int_values:
            self.assertEqual(self.Calculator.add(values['a'], values['b']), values['result'])

    def test_csvReader_subtraction(self):
        self.csv_reader = CsvReader('./src/subtraction.csv')
        for values in self.csv_reader.int_values:
            self.assertEqual(self.Calculator.add(values['a'], values['b']), values['result'])

    def test_csvReader_multiplication(self):
        self.csv_reader = CsvReader('./src/multiplication.csv')
        for values in self.csv_reader.int_values:
            self.assertEqual(self.Calculator.add(values['a'], values['b']), values['result'])

    def test_csvReader_division(self):
        self.csv_reader = CsvReader('./src/division.csv')
        for values in self.csv_reader.int_values:
            self.assertEqual(self.Calculator.add(values['a'], values['b']), values['result'])

if __name__ == '__main__':
    unittest.main()



