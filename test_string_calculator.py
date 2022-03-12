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
        self.assertRaises(ValueError,result)


#We don't need this as we will be using nosetests
# if __name__ == '__main__':
#     unittest.main()