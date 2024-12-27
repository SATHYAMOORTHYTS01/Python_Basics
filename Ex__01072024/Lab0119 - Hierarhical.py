# Hierarhical Inheritance

# ONE Father - Multiple children


class Father:
    def BHK1(self):   # self belongs to father
        print("BHK1")

class Sathya(Father):

    def BHK2(self):
        print("BHK2")

class Sathish(Father):

    def BHK3(self):
        print("BHK3")

class amit(Father):

    def no_house(self):
        print("No house")


Sathya = Sathya()
Sathya.BHK1()
Sathya.BHK2()

Sathish = Sathish()
Sathish.BHK1()
Sathish.BHK3()
# sathish.BHK2()  # Error - BHK2 is not defined in Sathish class

amit = amit()
amit.BHK1()
amit.no_house()
# amit.BHK2()  # Error - BHK2 is not defined in amit class
# amit.BHK3()  # Error - BHK3 is not defined in amit class

