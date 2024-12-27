
# 1. No return type no args/paramters
def say_hello():
    print("Hello")
say_hello()

# 2. No return with parameters

def say_hello_(name):
    print("Hello",name)
say_hello_(name="Sathya")

# 3. No return with default args

def say_hello_arg_default(name="Guest"):
    print("Hello", name)
say_hello_arg_default(name="Sathya")
say_hello_arg_default()

# 4. Return type with args
def say_hello_arg_return(name):
    return "Hello " + name
name = say_hello_arg_return("Sathya")
print(name)

