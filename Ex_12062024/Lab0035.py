from itertools import filterfalse

a = 10
b = 45
c = 44
d = 55

result1 = (a > b)  # False
result2 = (c < d)  # True
result3 = result1 and result2  # False and True = False - #AND OPERAOR ALSWAYS GUVES FALSE

# AND Gate
# false false  - false
# fasle true  - false
# true false  - false
# true true  - true
