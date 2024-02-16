# Classes and Objects Also Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks!")
    
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows!")


animals = [Dog("buddy"),Cat("whiskers")]
for animal in animals:
    animal.make_sound()

# Encapsulation
class BankAccount:
    def __init__(self,balance):
        self._balance = balance # Private Attribute
    def deposite(self,amount):
        self._balance += amount
    def get_balance (self):
        return self._balance
myacc = BankAccount(100)
myacc.deposite(50)
print(myacc.get_balance())

# Polymorphism
def greet(animal):
    animal.make_sound()
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    greet(animal)


# Abstarction: Hiding implementation details exposing only essential info and functinality of object
class Shape:
    def area(self):
        raise NotImplementedError  # Abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

shapes = [Circle(2), Square(5)]
for shape in shapes:
    print(f"Shape area: {shape.area()}")
