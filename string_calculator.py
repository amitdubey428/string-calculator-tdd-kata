class StringCalculator(object):
    def Add(self,x):
        x = x.strip()  
        if len(x) == 0:
            return len(x)
        if len(x) == 1:
            return int(x)