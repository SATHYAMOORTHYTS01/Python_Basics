# Recursion
##
# Recursion is a programming rechnique where a function --
# calls iteslf in order to solve aproblem
from math import factorial

# 1. Base case
# 2. Recursive case

# Factorial

def factorial(n):
    # base case :
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)

print(factorial(5))
