class StringCalculator(object):
    def Add(self,x):
        x = x.strip()
        if len(x) != 0:
            return int(x)
        return len(x)
            