set1 = set(["sathya.", " is for", "sathya"])

print(len(set1))

for i in set1:
    print(i)

set1 = set(["sathya.", " is for", "sathya","sathya", " is for", "sathya"])
print(set1)
set1.add("sandhya")
set1.remove("sathya")
print(set1)