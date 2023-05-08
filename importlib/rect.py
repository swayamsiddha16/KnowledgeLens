class Rect:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def getArea(self):
        print(self.length*self.breadth)
    
    def getPerimeter(self):
        print(2*(self.length + self.breadth))
        
        


