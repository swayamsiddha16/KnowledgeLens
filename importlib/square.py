class Square:
    def __init__(self, s):
        self.side = s
    
    def getArea(self):
        print(self.side**2)
    
    def getPerimeter(self):
        print(4*self.side)
