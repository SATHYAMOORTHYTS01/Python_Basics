# Filters in JavA

# python = vast = not al functions are required to built you
# Automation Tester - API snd WEB Automation

my_dict = \
    {

    'a':1,
    'c':3,
    'd':4
}
# To find a key in the dictionary

for k,v in my_dict.items():
    if k == 'c':
        print("key with the name c is found"
              ,k,v)

op1 = 'a' in my_dict
print(op1)  # output is always comes in True or False
op2 = 'b' in my_dict
print(op2)

op4 = 't' in my_dict
print(op4)

op3 = 'd' in my_dict
print(op3)