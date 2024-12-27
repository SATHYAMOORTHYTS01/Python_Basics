# Take the 2 int number from the user and we want to add them
# we need to use the input() function.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int --> ?int()
result = str(num1) + str(num2)
print(result)


# + -> int sum operation
# + -> str - concatenate
# int to str -> str()
# str to int -> int()

print(type(str(num1)))
print(type(int(num2)))
print(type(str(num1) + str(num2)))
print(type(int(num1) + int(num2)))

