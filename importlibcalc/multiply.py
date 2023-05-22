class Multiply:
    def __init__(self, l):
        self.l = l
       
    
    def doMultiply(self):
        Mul=1
        for i in range(len(self.l)):
            Mul = Mul * self.l[i]

        return Mul  