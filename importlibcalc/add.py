# class Add:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def doAdd(self):
#         print(self.a+self.b)

class Add:
    def __init__(self, l):
        self.l = l
       
    
    def doAdd(self):
         sum=0
         for i in range (0,len(self.l)):
             sum += self.l[i]
             
         return sum       
   