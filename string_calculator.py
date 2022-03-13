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
            numbers[:] = [int(x) if x != "" and int(x) <= 1000 else 0 for x in numbers] # Changes value of null strings and x>1000 to 0
            negative_list = list(filter(lambda x:x<0,numbers))
            if negative_list:
                raise Exception("negatives not allowed: {neg_list}".format(neg_list=negative_list))
            return sum(numbers)
        except ValueError:
            return("Oops not a number!")
        except Exception as e:
            return str(e)
            