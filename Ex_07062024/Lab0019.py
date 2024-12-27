#Strings

#In built function
#function -> Repeat a task - You can use a function
#print() -> Function
#type() -> Function
#input() -> Function
#format() -> Formatting
#max(), min(), id(), sum(), avg()


#Strings - collection of characters
name = "Sathya" # 0 to 5
#0,1,2,3,4,5
#S,a,t,h,y,a

name2 = 'Sathya'
name3 = """Sathya"""
print(name, name2, name3)
print(type(name), type(name2), type(name3))
print(id(name), id(name2), id(name3)) #id -> memory address where it is stored 4330240404
print(len(name), len(name2), len(name3))
# length of  string (1)

name = name.upper() #SATHYA
name = name.lower() #sathya

a = name.count('tear')
print(a)
print(name[4])
print(name[-1])
print(name[0:3])
print(name[3:6])
print(name[3:])



