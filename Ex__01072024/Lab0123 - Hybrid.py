# Hybrid Inheritacne

# hierarchical mix with multiple


class A:

    def methodA(self):
        return 'A method'

class C(A):

    def methodC(self):
        return 'C method'

# single becoming to hierarhical

class  B(A):

    def methodB(self):
        return 'B method'

class D(B, C):  # multiple, multilevel

    def methodD(self):
        return 'C method'


d = D()   # d has all the things it is the lower one who can get all
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
