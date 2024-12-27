class Father:

    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"

class Mother:

    def mother_money(self):
        return "10"

    def home(self):
        return "This is from the Mother"

class son(Father, Mother):
        pass

# Problem - Diamond problem - java
# Python - solvedd this problem in multiple inheritance

son = son()
son.father_money()
son.mother_money()
print(son.home()) # THIS WILL CALL whoever is in first - method resolution

