## map - return normal number
# pick 1 item and apply the function
# give the sam enumber of elements

numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(numbers):
    return numbers * 2

def even_giver(numbers):
    return numbers % 2 == 0

# new_list = list(map(lambda x: x*7, numbers))

double_numbers = map(double, numbers)
even_numbers = filter(even_giver, numbers)
print(list(even_numbers))
print(list(double_numbers ))


# Filters -   only work with function true or false

# pick item if true keep ut, false, remove it
# it can give less number of elements as compared to actual list


def even_given(numbers):
    return numbers % 2 == 0

new_filtered_list = list(filter(even_given, numbers))
print(new_filtered_list)

new_filtered_list = list(filter(lambda x: x%2 == 0, numbers))
print(new_filtered_list)