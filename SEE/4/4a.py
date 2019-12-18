class Rectangle:
    le=0
    br=0
    def __init__(self,a,b):
        self.le = a
        self.br = b
    def Area(self):
        self.answer = self.le * self.br
        return self.answer
obj = Rectangle(2,3)
print(obj.Area())