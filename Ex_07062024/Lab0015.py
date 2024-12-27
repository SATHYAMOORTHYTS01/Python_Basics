# Write a program to take two integer number from user and add them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2  # this will concatenate the two strings
print(sum)
# so to get the sum of the two numbers we need to convert them to int
#sum = int(num1) + int(num2)
#print(sum)

int()  # this will convert the string to integer
float()  # this will convert the string to float
str()  # this will convert the integer to string

sum = float(num1) + float(num2)
print(sum)
print(type(sum))