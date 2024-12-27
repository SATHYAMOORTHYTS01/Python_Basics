# User defined
# They can return something
# They cant return nothing
# They have parameters
# They don't have parameters / arguments


def say_hello():  # no return type and no parameter/args
    print("Hello")
say_hello()


def say_hello(name):  # no return type but with parameter/args
    print("Hello", name)

say_hello("Mani")  # calling the function with args
say_hello("Kumar")  # calling the function with args


def say_hello_arg_default(name="Guest"):  # with default value
    print("Hello", name)


say_hello_arg_default()  # it will pick Guest
say_hello_arg_default("Mani")  # it will pick Mani
say_hello_arg_default("Kumar")  # It will  pick Kumar


def sum_number_argument_return(a, b):
    return a + b
number = sum_number_argument_return(10, 20)
print(number)
