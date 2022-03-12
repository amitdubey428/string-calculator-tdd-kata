import unittest

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

    #Test Case for just 1st instruction as it states "upto 2 numbers"
    def test_addition_max_two_numbers(self):
        result = calc.Add("1,2,3")
        self.assertEqual("Oops you can add only two numbers!",result)

#We don't need this as we will be using nosetests
# if __name__ == '__main__':
#     unittest.main()