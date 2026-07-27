class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(f"A+B={self.num1+self.num2}")
    def subtract(self):
        print(f"A-B={self.num1-self.num2}")
    def multiply(self):
        print(f"A*B={self.num1*self.num2}")
    def divide(self):
        if self.num2==0:
            print("Division is not possible")
        else:
            print(f"A/B={self.num1/self.num2}")
c1=calculator(20,10)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()
