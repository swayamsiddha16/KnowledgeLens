class Divide:
    def __init__(self, l):
        self.l = l
       
    
    def doDivide(self):
         quot=1
         for i in range (0,len(self.l)):
             quot = quot / self.l[i]
             
         return quot