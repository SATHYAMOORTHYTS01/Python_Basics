# Decorators
# What is decorator?
# Decorators are a way to modify the behavior of a function or class without changing its source code.
def my_decorator(func):
    def wrapper():
        print("Starting......")
        print("..................")
        func()
        print("................")
        print("End......")
    return wrapper()

@my_decorator
def say_hello():
    print("Say Hello!")

