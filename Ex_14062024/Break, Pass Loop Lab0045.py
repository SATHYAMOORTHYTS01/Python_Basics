# Break -> Based on condition it will break the loop
for i in range(10):
    if i == 6:
        break
    else:
        print(i)

# Pass -> Skips the current iteration
for i in range(1, 10):
    if i == 5:
        pass
    else:
        print(i)
