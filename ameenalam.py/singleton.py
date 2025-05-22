""""singleton means aik class m aik object"""
class Order():
    isInstance =None
    def __new__ (cls,*args,**kwargs):#cls refers to the class itself that is being used to create the objectSo if you're calling Order(), then cls is Order."""
        print(Order.__new__)
        if cls.isInstance == None:
            cls.isInstance=super().__new__(cls)
            return cls.isInstance
    def __init__(self,id,amount,kg):
        self.id=id
        self.amount=amount
        self.kg=kg
        
chai=Order("01",76,5)
chai2=Order("02",89,98)
print(chai)
print(chai.id)
print(chai2.id)