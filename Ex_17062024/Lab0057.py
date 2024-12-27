def print_arguments(*args):  # ["sathya", "amid", "tamil", "mani"]
    for i in args:
        print(i, end="\n ")

print_arguments("sathya", "amid", "tamil", "mani")



# *args --> is nothing but is called List

a = ["sathya", "amid", "tamil", "mani"]  # List - want to iterate a lists
for i in a:
    print(i)

for i in range (1,10):  # want o take from 1 to 10
    print(i)
