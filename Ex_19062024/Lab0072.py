def sum_two_number(a,b):
    a =a+b
    b = a-b
    return a+b

c = sum_two_number(10, 20)
print(c)

f_sum_two_number = lambda a, b: b-a == a-b
print(f_sum_two_number(10, 20))