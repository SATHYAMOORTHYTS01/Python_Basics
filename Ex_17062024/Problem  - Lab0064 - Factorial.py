# Factorial
import math
from math import factorial
from operator import matmul

n = 5
factorial = 1
# result = math.factorial(5)
# print(result)

while n>0:
    factorial = factorial * n
    n = n-1
print(factorial)

# While loop Debugging
#
# n = 5
# factorial = 1

# # 1st statement
# 5> 0 - yes
# factorial = 1*5 = 5
# n = 5-1 = 4
#
# # 2nd statement
# n = 4, f=1
# 4>0 - yes
# factorial = 1*4 = 4
# n = 4-1 = 3
# # 3rd statement
# n = 3, f=1
# 3>0 - yes
# factorial = 1*3 = 3
# n = 3-1 = 2
# # 4th statement
# n = 2, f=1
# 2>0 - yes
# factorial = 1*2 = 2
# n = 2-1 = 1
# # 5th statement
# n = 1, f=1
# 1>0 - yes
# factorial = 1*1 = 1
# n = 1-1 = 0
# # 6th statement
# n = 0, f=1
# 0>0 - no


for i in range (1, n+1): # goes from 1,2,3,4,5
    factorial = factorial * n
print(factorial)


# For loop Debugging

# for i in range (1, n+1): # goes from 1,2,3,4,5
    factorial = factorial * i

   # here n+1 means , our values are 1,2,3,4,5 in python elelment 5 will not be taken
   # so, in need of 5 in last n+1 , 5+1 = 6
   # then our values will be 1,2,3,4,5,6 , here 6 will be consideredd will get a 5 values

i =1
f = 1

# 1st execution 1
factorial = factorail * i # 1*1 = 1
fact = 1

# 2nt execution 2  # i = incremented to 2 , fact =1
factorial = factorail * i # 1*2 = 2
fact = 2

#  3rd execution 3 # i = incremented to 3 , fact =2
factorial = factorail * i # 2*3 = 6

# 4th execution 4 # i = incremented to 4 , fact =6
factorial = factorail * i # 6*4 = 24

# 5th execution 5 # i = incremented to 5 , fact =24
factorial = factorail * i # 24*5 = 120
