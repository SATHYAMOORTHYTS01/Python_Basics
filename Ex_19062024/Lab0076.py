# List
a = [1, 2, 3, 4, 5]

# Indexing
print(a[0])  # Output: 1

# append
a.append(6)
print(a)  # Output: [1, 2, 3, 4, 5, 6]

# extend
a.extend([7, 8, 9])
print(a)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert
a.insert(0, 9)
print(a)  # Output: [9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove
a.remove(9)
print(a)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# changing the value
a[0] = 10
print(a)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# pop
a.pop(2)  # remove the last element
print(a)  # Output: [10, 2, 4, 5, 6, 7, 8, 9]

# del
del a[0]  # remove the first element
print(a)  # Output: [2, 4, 5, 6, 7, 8, 9]

# copy
list
b = a.copy()  # copy the list a to b
print(b)  # Output: [2, 4, 5, 6, 7, 8, 9]

# sort
a.sort()  # sort the list in ascending order
print(a)  # Output: [2, 4, 5, 6, 7, 8, 9]

# reverse
a.reverse()  # reverse the list
print(a)  # Output: [9, 8, 7, 6, 5, 4, 2]



