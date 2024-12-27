# Decorators
# A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying the function source code.

def my_decorator(func):
    def wrapper():
        print("Starting......")
        print("..................")
        func()
        print("................")
        print("End......")

    return wrapper()
# What is decorator?
# Decorators are a way to modify the behavior of a function or class without changing its source code.

# wrapper is used for



def my_decorator(func):
    def wrapper():
        print("Starting......")
        print("..................")
        func()
        print("................")
        print("End......")

    return wrapper()


@my_decorator  # A ANNOATION we added
def say_hello():
    print("Say Hello!")


