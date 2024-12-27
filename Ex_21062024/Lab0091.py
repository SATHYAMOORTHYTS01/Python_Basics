my_dict = {'e': 1, 'w': 2, 'c': 3, 'a': 4}
print(my_dict)

for k,v in my_dict.items():
    print(k,v)
print(f"Key={k}, Value={v}")

my_dict['a'] = 40
my_dict['d'] = 50
my_dict['e'] = 60
my_dict['f'] = 70
print(my_dict)

for k,v in my_dict.items():
    print(k, v)
    if k == 'c':
        break
        print("Loop Breaked")

