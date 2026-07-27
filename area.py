class areaofrec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("the area of rectangle is:",self.l*self.b)
obj1=areaofrec(40,50)
obj2=areaofrec(7,8)
obj1.area()
obj2.area()
