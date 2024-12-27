##

sathya_details = {
    "name": "Sathya",
    "age": 24,
    "gender": "male",
    "is_married": "Yes",
    "Address": "TN:",
}

print(sathya_details.get("name"))
print(sathya_details.get("age")) # we dont have index for finding a value instead we have keys
print(sathya_details.values())
print(sathya_details.keys())

my_dict = { 'a':1,  'b':2, 'c':3, 'a':4, 'd': 2}
# duplicte values is removed then latest  value is taken
# values can be duplicate but keys are unique
print(my_dict)
print(len(my_dict))
print(list(my_dict.values()))# values in list format
print(list(my_dict.keys()))# keys in list format

for k,v in my_dict.items():
    print(k,v)


