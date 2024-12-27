class Person:
    # class variables / instance variables
    name = "John"
    age = 30

    def walk(self):
        a = 10 # local variable
        print("Hello my name is ", self.age)


# Object creaion
John = Person()
John.walk()


