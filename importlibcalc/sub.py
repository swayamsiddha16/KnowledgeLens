class Sub:
    def __init__(self, l):
        self.l = l
       
    
    def doSubtract(self):
         diff=0
         for i in range (0,len(self.l)):
             diff -= self.l[i]
             
         return diff     