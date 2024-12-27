class person:
    # Attribute
    name = None
    id = None
    age = None
    phone = None
    address = None

    # Behaviour
    # - beahviour are created with function

    def walk(self): # NO arg, No return
        print("I am walking")

    def eat(self, name): # 1 arg and no return type
        print("I am eating")
        print("eat",name)

    def sleep(self, name):  # 1 args and 1 return type
        print("I am sleeping")
        return None

    def talk_return(self): # No Arg with Return Type
        return "I am talking"



# ---- till here it was a class

# Create Object of the person class
# ObjectRef -> Object -> ClassName()
surya =  person()
surya.name = "Surya"
surya.walk() # calling the behaviour of the class using the object of the class (dot operator is used

ritika = person()
ritika.name = "Ritika" # . ddot is used o access the attribute of the class
ritika.eat()