# Method Overloading
#  Same method name with different arguments
# Python does not support method overloading

class Test:
    def m1(self, a, b =0, c=0):
        return a+b+c

    # def m1(self, a):
    #     print(a)

test = Test()
op1 = test.m1(10)
op2 = test.m1(10, 20)
op3 = test.m1(10, 20, 30)
print(op1)
print(op2)
print(op3)
