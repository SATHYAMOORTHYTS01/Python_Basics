# lambda arguments: expression

def finf_odd_even(num):
    if num%2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
    print(finf_odd_even(10))


finf_odd_even = lambda num: "The number is even" if num%2 == 0 else "The number is odd"
print(finf_odd_even(10))

