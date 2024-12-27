x = 10
q, w, e = (23, 22, 33)

print(e) #
print(q)
print(w)

#Tuple is assigned to the diff diff variables

# Search in tuple
tuple1 = ("london",  "paris", "tokyo", "new york")
print("paris" in tuple1)
print("shanghai" in tuple1)

t = (1,2,3,4,5,)
# simpley we can use append in tuple like t.append
#t.append() tuple are immutable in nature

#another way is there like

new_t = t + (11,) # append - we can add another element in the tuple
print(new_t)

# IF you want convert the tuple in list - add append then conevrt the  list to new tuple

my_list = list(t)
print(my_list)
my_list.append(11)
my_list.append(22)
new_t2 = tuple(my_list)
print(new_t2)
