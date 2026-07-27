class Hospital:
    Location="Amritsar"
    def __init__(self,name,age,problem):
        self.name = name
        self.age =age
        self.problem=problem

patient1= Hospital("Karan", 21 ,"ortho")
patient2= Hospital("Jashan", 21 ,"psyco")

print(patient1.name)
    