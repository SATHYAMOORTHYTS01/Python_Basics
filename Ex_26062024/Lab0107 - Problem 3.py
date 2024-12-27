##
#
class Person:
    # constructor with attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Behaviour
        def sleep(self):
            print("Who is  Sleeping" + self.name + " " + self.id )


def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects and invoking the constructor
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Invoking object method