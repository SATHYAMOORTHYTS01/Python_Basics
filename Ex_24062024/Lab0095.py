numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(numbers):
    return numbers * 2

def even_giver(numbers):
    return numbers % 2 == 0

# new_list = list(map(lambda x: x*7, numbers))

double_numbers = map(double, numbers)
print(list(double_numbers ))
even_numbers = filter(even_giver, numbers)
print(list(even_numbers))


##
