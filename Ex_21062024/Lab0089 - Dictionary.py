# Dictionary to store the count of each character
# key and value
# A dictionary is an unorderes collection of data
# In a key value format.
# Mutable in nature

dic = {}
# name -> "ram"
my_dict = {"name": "ram", "age": 23, "address": "kathmandu"}
print(my_dict["name"])
my_dict["name"] = "shyam"
print(my_dict)
print(my_dict["age"])
print(my_dict["address"])

# We can wrtie without " "

phone_book = dict(
    ram="9812345678",
    shyam="9812345679",
    hari="9812345670")
print(phone_book["ram"])




