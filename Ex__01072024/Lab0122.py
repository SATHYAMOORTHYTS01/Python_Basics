class A:

    def method(self):
        return 'A method'

class B:

    def method(self):
        return 'B method'

class C(A, B):
    pass

c = C()
print(c.method())