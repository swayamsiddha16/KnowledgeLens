class Shapes:
    def __init__(self):
        print("Instance created")
class square(Shapes):
    def __init__(self,s):
        self.side=s
    def getArea(self):
        print(self.side**2)
    def getPerimeter(self):
        print(2*((self.length)+(self.breadth)))
class rect(Shapes):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def getArea(self):
        print(self.length*self.breadth)
    def getPerimeter(self):
        print(4*((self.length*self.breadth)))
    
shape =input("Enter the type of shape : ")

if shape == "rect":
    obj1=rect(12,10)
    obj1.getArea()
    obj1.getPerimeter()
elif shape == "square":
    obj2 = square(12)
    obj2.getArea()
    obj2.getPerimeter()
    