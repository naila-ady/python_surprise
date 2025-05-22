class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+ self.num2
    def subtract(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return self.num1 /self.num2
    def show_All(self):
        return(
        f"Addition:{self.add()}\n"
        f"Subtraction:{self.subtract()}\n"
        f"Multipliation:{self.multiply()}\n"
        f"Division:{self.divide()}")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

                
obj1=Calculator(num1,num2)
obj1.add()
print(obj1)#this will print only the referrnce 
print(obj1.add())
print(obj1.subtract())
print(obj1.multiply())
print(obj1.divide())
print(obj1.show_All())
