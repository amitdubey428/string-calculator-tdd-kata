import re


class StringCalculator(object):
    def Add(self,numbers):
        """
        Add numbers from a string, seperated by delimiters

        Args:
            String: String containing single or multiple numbers seperated by delimiters

        Returns:
            Int: Sum of the numbers present in the string
        """
        
        default_delimiter = ',|'
        long_delimiter_regex = re.compile("^//\[.*\]\\n")  # regex to check for long delimiter
        
        try:
            numbers = numbers.strip()
            if "//" in numbers and numbers.index("//") == 0:  ## Outer if to check custom delimiter  
                if long_delimiter_regex.match(numbers):  ## To check long delimiter
                    default_delimiter=""
                    delimiter_match = long_delimiter_regex.match(numbers).group()[3:-2]
                    for x in delimiter_match:
                        default_delimiter+= (re.escape(x)) + "|"
                    numbers = numbers[long_delimiter_regex.search(numbers).end():]
                else:
                    default_delimiter = str(numbers[2])+"|"
                    numbers = numbers[numbers.index("//")+3:]

            delimiter_regex = default_delimiter+"\n"
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
            