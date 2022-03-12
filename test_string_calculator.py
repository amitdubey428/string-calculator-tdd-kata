import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_addition(self):
        calc = StringCalculator()
        result = calc.Add("")
        self.assertEqual(0,result)


#We don't need this as we will be using nosetests
# if __name__ == '__main__':
#     unittest.main()