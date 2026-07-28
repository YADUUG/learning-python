give_command= int(input("enter the command: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
def calc(a,b):
    if give_command == 1:
        return a+b
    elif give_command == 2:
        return a-b
    elif give_command == 3:
        return a*b
    else:
        return a/b
    
print(calc(8,6))
