import re


class StringCalculator(object):
    def Add(self,numbers):
        default_delimiter = ','
        try:
            numbers = numbers.strip()
            if "//" in numbers and numbers.index("//") == 0:
                default_delimiter = str(numbers[2])
                numbers = numbers[3:]
            delimiter_regex = default_delimiter+"|\n"
            numbers = re.split(delimiter_regex,numbers)
            numbers[:] = [x if x != "" else 0 for x in numbers] # Changes value of null strings to 0
            int_list = list(map(int,numbers))
            return sum(int_list)
        except ValueError:
            return("Oops not a number!")
            