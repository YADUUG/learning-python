class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
         self.balance+=amount
         print("balance after deposit",self.balance)
         
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient balance ")
        else:
            self.balance-=amount
            print("The balance after withdrawal is:",self.balance)
    def display(self):
        print("Final balance is:",self.balance)
        
balance=int(input("Enter the balance"))
dep_amount=int(input("Enter the deposit amount"))
obj=bank(balance)
obj.deposit(dep_amount)
with_amount=int(input("Enter the withdrawal amount"))
obj.withdraw(with_amount)
obj.display()

