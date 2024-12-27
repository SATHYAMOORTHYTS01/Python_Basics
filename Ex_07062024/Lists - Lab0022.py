# List - what is list?
# List is a collection of items in a particular order.
# 1. Add item
# 2.Remove item
# 3.append item
# 4.view item
# 5.exit
#
# How to define a list?
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
print(len(my_list))
print(id(my_list))
print(my_list[0])
print(my_list[4])
print(my_list[-1])
print(my_list[-5])

my_list.append(3) # ADD ITEM IN THE END - add only one item
print(my_list)
my_list.insert(0, 10) # ADD ITEM IN THE BEGINNING
print(my_list)
my_list.remove(3) # REMOVE ITEM FROM THE LIST
print(my_list)
my_list.pop() # REMOVE LAST ITEM FROM THE LIST
print(my_list)
my_list.extend([9, 8, 7]) # ADD MULTIPLE ITEMS TO THE LIST - extends a list
print(my_list)
my_list.sort() # SORT THE LIST
print(my_list)
my_list.reverse() # REVERSE THE LIST
print(my_list)
print(my_list.index(5))
my_list.clear() # CLEAR THE LIST
print(my_list)




