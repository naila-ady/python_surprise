class Account:
    def __init__ (self,balance):
        self.__balance= balance#private
    
    def get_balance(self):
        return self.__balance
acc=Account(100000)
print(acc.get_balance())
# print(acc.__balance)


class Person:
    def __init__(self, name):
         self._name = name  # protected attribute
    def display_name(self):
        print(f"Name: {self._name}")
p = Person("Alice")
p.display_name()
print(p._name)
 

