 # Ternary operator

sathya = 30
amid  = 33

print(sathya) if sathya > amid else print(amid)
print("Sathya" if sathya > amid else "Amid")
print("Sathya") if sathya > amid else print("Amid")
print("Sathya" if sathya > amid else "Amid")

if sathya > amid:
    print("Sathya")
    print("Sathya is greater")
else:
    print("Amid")
    print("Amid is greater")
