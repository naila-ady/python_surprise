"""object.__new__(cls)
object → The top-level base class in Python. Every class inherits from it (unless you say otherwise).
__new__ → A class method defined in object that creates a new object.
cls → The class you're trying to instantiate (e.g., Order, MyClass, etc.). Not an instance it’s the class itself
“Use the default constructor from the base class object to create a new instance of the class cls.”
"""
class Order():
    def __new__(cls ,*args ,**kwargs):
        print("")
        return super().__new__(cls)
    def __init__(self ,id:str="", amount:float=0.0, weight:float=0,):
        self.id=id
        self.amount=amount
        self.weight = weight
        
order1=Order
# print(dir(Order))
print(type(order1))
print(dir(order1))