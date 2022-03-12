class StringCalculator(object):
    def Add(self,x):
        try:
            x = x.strip()
            if len(x) != 0:
                return int(x)
            return len(x)
        except ValueError:
            return("Oops not a number!")
            