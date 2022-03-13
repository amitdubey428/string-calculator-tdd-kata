import re


class StringCalculator(object):
    def Add(self,numbers):
        try:
            numbers = numbers.strip()
            numbers = re.split('[, \n]',numbers)
            numbers[:] = [x if x != "" else 0 for x in numbers]
            int_list = list(map(int,numbers))
            return sum(int_list)    
        except ValueError:
            return("Oops not a number!")
            