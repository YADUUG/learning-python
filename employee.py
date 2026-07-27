class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("The name of employee is",self.name)
        print("Salary is",self.salary)
e=employee("harry",15000)
e.show()
