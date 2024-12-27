class Dog:
    # Attributes

    name = None # None - Default value
    breed = None
    age = None
    color = None

    def __init__(self,name,id): # Constructor __ - private method
        self.name = name
        self.id = id

     # constructor?
     #  Use to initialize the values of the instance variables (Attributes)



    #  Behaviour
    def sleep(self):
        print("zzz Sleeping")
    def eat(self):
        print("Eating")


# Object creation

dog1 = Dog() # Object creation
print(dog1.name)
dog1.name = "Tommy" # Assigning the value to the attribute
print(dog1.name)
dog1.sleep()

dog2 = Dog() # Object creation
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)

