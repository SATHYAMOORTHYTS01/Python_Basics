class Car:
    name = None


    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"

# public method - is availabel everywhere
    def printname(self):
        print("Public method called")

#### private things are allowed within the class
    # printname is within the class
    # __private_var is accesbile  by printname method only


    def printname(self): # this function can access the private variable
        if self.__private_var == "pass@123":
            print("Private method called")

# This line is end of the class

alto = Car()
alto.printname()
print(alto.public_var)

# alto.__private_method() # outside not accessible


