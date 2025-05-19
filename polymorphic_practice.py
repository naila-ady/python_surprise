class Employee():
    def get_salary():
        pass
class Manager(Employee):
    def get_salary(self):
        return 80000
class Developer(Employee):
    def get_salary(self):
        return 60000
class Intern(Employee):
    def get_salary(self):
        return 20000
salaries =[Manager() ,Developer() ,Intern()]
for salary in salaries:
    print(salary.get_salary())

    