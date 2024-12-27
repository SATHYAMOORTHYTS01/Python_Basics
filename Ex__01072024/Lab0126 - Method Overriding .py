# Method overriding - same method name with different implementation in child class
# child always oveeride the parent funtions
# super means call my parent function

# it does not give output of father
# instead of that we are using super to call the parent function


# Example 1
# Parent class
class Father:

    def home(self):
        print("1BHK")

# child class
class Son(Father):
    def home(self):
        super().home() # super is used to calling the parent function 
        print("No House")


satya = Son()
satya.home()
