class StringCalculator(object):
    def Add(self,numbers):
        try:
            numbers = numbers.strip()
            if len(numbers) != 0:
                numbers = numbers.split(",")
                int_list = list(map(int,numbers))
                if len(int_list) <=2:
                    return sum(int_list)
                return("Oops you can add only two numbers!")
            return len(numbers)
        except ValueError:
            return("Oops not a number!")
            