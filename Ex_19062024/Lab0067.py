# Function scope
# function is defined and called - block of code and code is resued
# types of functions - buit in functions, user defined functions

def add():
    a = 10
    b = 20
    c = a+b
    local variable
    print(b)

my_function = add() # calling the function
print(my_function) # None - as function does not return any value, it returns None by default