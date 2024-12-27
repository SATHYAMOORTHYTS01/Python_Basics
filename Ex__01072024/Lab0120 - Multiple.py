# Multiple inheritance

# MEANS father and mother are there

# And son will inherit from both of them

class Father:
    def BHK1(self):
        print("BHK1")

class Mother:
    def BHK2(self):
        print("BHK2")

class Son(Father, Mother):
    pass

son = Son()
son.BHK1()
son.BHK2()
print(son)
