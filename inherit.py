class Animal:
    def sound(self):
        print("some generic sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    pass
dog=Dog()
cat =Cat()
dog.sound()
cat.sound()#it will inherit the functions and method of parent class


class Vehicle:
    def start(self):
        print("Start Vehicle")
class Car(Vehicle):
    def start(self):
        super().start()
        print("starting the car")
class ElectricCar(Car):
    def start(self):
        print("starting Electric car Silently")
print("for Mustafa car")       
muscar=ElectricCar()
muscar.start()#it will
print("for alicar")
alicar=Car()
alicar.start()        
print("for adnan car")
adn_car=Vehicle()
adn_car.start()