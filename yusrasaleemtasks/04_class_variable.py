class Counter:
    count = 0 #class level variable
    def __init__ (self):
        Counter.count +=1
    @classmethod
    def display_count(cls):
        return f"Total objects created: {cls.count}"  # Returning the count
# When you create an object of the Counter class:
obj1=Counter()# Calls the __init__ method, incrementing Counter.count
obj2=Counter()
obj3=Counter()

result=Counter.display_count()
print(result)