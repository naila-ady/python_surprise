class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.grade=grade
        self.age=age
    def get_dispaly(self):
        return f" Student {self.name} age is {self.age} and grade is {self.grade} "
stud1=Student("ali",8 ,"lV")
print(stud1.get_dispaly())

    