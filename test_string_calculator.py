import unittest
from unittest import result

from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    
    global calc
    calc = StringCalculator() #calc object to be used for all test cases
    
    def test_empty_addition(self):
        result = calc.Add("")
        self.assertEqual(0,result)

    def test_white_space_addition(self):
        result = calc.Add(" ")
        self.assertEqual(0,result)

    def test_addition_one_number(self):
        result = calc.Add("1")
        self.assertEqual(1,result)

    def test_addition_not_a_number(self):
        result = calc.Add("a")
        self.assertEqual("Oops not a number!",result)

    def test_addition_two_numbers(self):
        result = calc.Add("3,6")
        self.assertEqual(3+6,result)
    
    def test_addition_two_containing_alphabet(self):
        result = calc.Add("1,a")
        self.assertEqual("Oops not a number!",result)

    def test_addition_with_white_space(self):
        result = calc.Add("2 , 4 ")
        self.assertEqual(2+4,result)
    
    def test_addition_with_empty_commas(self):
        result = calc.Add(" , ")
        self.assertEqual(0,result)

    def test_addition_with_one_empty_commas(self):
        result = calc.Add(" 2, ")
        self.assertEqual(2,result)

    def test_addition_with_white_spaces_in_between(self):
        result = calc.Add(" 3 , 5 ")
        self.assertEqual(3+5,result)

    def test_addition_with_new_line(self):
        result = calc.Add( "1\n2,3")
        self.assertEqual(1+2+3,result)

    # Test Case for just 1st instruction as it states "upto 2 numbers"
    # def test_addition_max_two_numbers(self):
    #     result = calc.Add("1,2,3")
    #     self.assertEqual("Oops you can add only two numbers!",result)

    def test_addition_max_two_numbers(self):
        result = calc.Add("4,7,2, 6")
        self.assertEqual(4+7+2+6,result)

    def test_addition_custom_delimiter(self):
        result = calc.Add("//;\n1;2")
        self.assertEqual(1+2,result)

    def test_addition_custom_delimiter_hyphen(self):
        result = calc.Add("//-4-5-9")
        self.assertEqual(4+5+9,result)

    def test_addition_with_single_negative(self):
        result = calc.Add("//!4!-5!9")
        self.assertEqual("negatives not allowed: [-5]",result)

    def test_addition_with_multiple_negatives(self):
        result = calc.Add("4,-5,-9,11,-10")
        self.assertEqual("negatives not allowed: [-5, -9, -10]",result)

    def test_addition_bigger_than_1000(self):
        result = calc.Add("2,1001")
        self.assertEqual(2,result)
        
#We don't need this as we will be using nosetests
# if __name__ == '__main__':
#     unittest.main()