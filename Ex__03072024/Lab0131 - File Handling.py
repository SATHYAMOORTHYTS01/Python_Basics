# File handling
#  This program demonstrates how to read from a file and write to a file

# # Open the input file in read mode
# file = open("input.txt", "r")
# # Read the contents of the file
# content = file.read()
# # Close the file
# file.close()
# # Open the output file in write mode
# file = open("output.txt", "w")
# # Write the contents to the output file
# file.write(content)

import os

# Print the current working directory
print(os.getcwd())

# Store the current working directory in a variable
cwd = os.getcwd()

# Open the file using the correct path format
with open(r"D:\PythonAT\PyLearning3xAT\Ex__03072024\New test data.py", 'r') as file:
    content = file.read()
    print(content)
