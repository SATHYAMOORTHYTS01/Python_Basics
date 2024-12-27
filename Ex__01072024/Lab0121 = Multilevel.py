# Base class (Parent class)
class Animal:
    def __init__(self):
        print("Animal is created")

    def eat(self):
        print("Animal is eating")

# Derived class inheriting from Animal (Child class)
class Mammal(Animal):
    def __init__(self):
        super().__init__()  # Calling the constructor of the Animal class
        print("Mammal is created")

    def give_birth(self):
        print("Mammal gives birth to live young")

# Another derived class inheriting from Mammal (Grandchild class)
class Dog(Mammal):
    def __init__(self):
        super().__init__()  # Calling the constructor of the Mammal class
        print("Dog is created")

    def bark(self):
        print("Dog is barking")

# Create an object of the Dog class
dog = Dog()

# Calling methods from each class in the inheritance chain
dog.eat()         # Inherited from Animal
dog.give_birth()  # Inherited from Mammal
dog.bark()        # Defined in Dog
