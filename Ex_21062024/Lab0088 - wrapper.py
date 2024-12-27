### wrapper is  a decorator that takes a function as an argument
def wrapper(func):
    def inner(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return inner
@wrapper
def hello():
    print("Hello")

