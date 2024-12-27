# Exceptions
# Exceptions are errors that occur during the execution of a program.
# They interrupt the normal flow of the program and allow the programmer to handle the error appropriately.
# Exceptions are handled using try-except blocks.

# SyntaxError: invalid syntax
    # The error is caused by the missing parentheses in the print statement.
#  print "Hello World"

# NameError: name 'print' is not defined
    # The error is caused by the missing quotation marks around the string.
# print 'Hello World'

# IndexError: list index out of range
    # The error is caused by trying to access an index that is out of range in a list.
my_list = [1, 2, 3]

# ZeroDivisionError: division by zero
    # The error is caused by dividing a number by zero.
num = 10

# KeyError: 'age'
    # The error is caused by trying to access a key that does not exist in a dictionary.
my_dict = {'name': 'John', 'age': 30}

# AttributeError: 'int' object has no attribute 'lower'
    # The error is caused by calling a method on an object of a different type.
my_str = 123

#  TypeError: can only concatenate str (not "int") to str
    # The error is caused by trying to concatenate an integer with a string.
my_str = 'Hello'
