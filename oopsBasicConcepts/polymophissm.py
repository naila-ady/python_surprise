#1st qusetion
# Bird naam ka ek class banaya gaya hai
class Bird:
    # sound() method define kiya gaya hai jo "Chirp" print karega
    def sound(self):
        print("Chirp")

# Duck class banayi gayi hai jo Bird class se inherit kar rahi hai (waris hai)
class Duck(Bird):
    # Duck apna khud ka sound() method define kar raha hai (override kar raha hai Bird ka method)
    def sound(self):
        print("Quack")

# make_sound naam ka function banaya gaya hai
# yeh function kisi bhi object ko accept karega jisme sound() method ho
def make_sound(bird):
    bird.sound()  # object ka sound() method call kiya ja raha hai

# Bird class ka object banaya aur b variable mein rakha
b = Bird()

# Duck class ka object banaya aur d variable mein rakha
d = Duck()

# make_sound function ko Bird object ke saath call kiya
# Yeh print karega: "Chirp"
make_sound(b)

# make_sound function ko Duck object ke saath call kiya
# Yeh print karega: "Quack"
make_sound(d)

#2nd question
class Shape:
    def area(self):
        pass  # This is a placeholder, meant to be overridden

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5  # Circle's own version of area

class Square(Shape):
    def area(self):
        return 5 * 5  # Square's own version of area

    #Circle() and Square() are  not calling a method, it's calling the class constructor.Behind the scenes, it’s 
    # like calling __init__() to initialize a new object.

shapes = [Circle(), Square()]# List of different Shape objects.Circle and Square both override the area() 
                            #method from the base class Shape.
for shape in shapes:
    print(shape.area())# Calls the appropriate area() based on object type

