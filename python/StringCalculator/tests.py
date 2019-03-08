import unittest
from StringCalculator import StringCalculator, NegativeException

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        result = calc.add("")
        self.assertEqual(0, result)

    def test_string_one_returns_one(self):
        calc = StringCalculator()
        result = calc.add("1")
        self.assertEqual(1, result)

    def test_string_one_comma_two_returns_three(self):
        calc = StringCalculator()
        result = calc.add("1,2")
        self.assertEqual(3, result)
    
    def test_string_supports_infite_number_of_numbers(self):
        calc = StringCalculator()
        result = calc.add("1,2,3")
        self.assertEqual(6, result)

    def test_support_newline_as_delimiter(self):
        calc = StringCalculator()
        result = calc.add("1\n2,3")
        self.assertEqual(6, result)

    def test_support_custom_delimiter(self):
        calc = StringCalculator()
        result = calc.add("//;\n1;2")
        self.assertEqual(3, result)

    def test_support_multiple_custom_delimiter(self):
        calc = StringCalculator()
        result = calc.add("//[*][%]\n1*2%3")
        self.assertEqual(6, result)

    def test_support_any_lenght_custom_delimiter(self):
        calc = StringCalculator()
        result = calc.add("//[***]\n1***2***3")
        self.assertEqual(6, result)        

    def test_negative_numbers_throw_exception(self):
        calc = StringCalculator()
        try:
            calc.add("-1,-2")
            self.fail()
        except NegativeException as ex:
            self.assertEqual(ex.args[0], "Negatives not allowed: -1,-2")

    def test_numbers_above_1000_are_ignored(self):
        calc = StringCalculator()
        result = calc.add("2,1001")
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()
