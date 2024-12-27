# Filters in python - e used to filter a sequence of elements based on a condition
# The filter() function in puthon is a built-in-funcion
# allows you to filter element in the list,tuple,set.

numbers = [1,2,3,4,5,6,7,8,9,10]
# filter on the above -> even numbers
# new_list_even = [2,4,6,8,10]


def is_even(num):
    return num % 2 == 0

new_numbers_even = filter(is_even,numbers)
print(list(new_numbers_even))

def is_greater_than_5(num):  # is_greater_than_5 - is a function
    return num > 5

new_numbers_greater_than_5 = filter(is_greater_than_5, numbers)
print(list(new_numbers_greater_than_5))

def is_lower_than_5(num):
    return num < 5
new_numbers_lower_than_5 = filter(is_lower_than_5, numbers)
print(list(new_numbers_lower_than_5))


