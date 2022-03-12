class StringCalculator(object):
    def Add(self,numbers):
        try:
            numbers = numbers.strip()
            numbers = numbers.split(",")
            numbers[:] = [x if x != "" else 0 for x in numbers]
            int_list = list(map(int,numbers))
            if len(int_list) <=2:
                return sum(int_list)
            return("Oops you can add only two numbers!")
        except ValueError:
            return("Oops not a number!")
            