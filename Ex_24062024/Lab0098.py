def sum_of_digis(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        n = n // 10 # quotient
        # / - divide
        # // -- quotient
        # % - remainder
        return sum_digits

print(sum_of_digis(12345))

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
        n = n // 10  # Remove the last digit from n
    return reversed_num

print(reverse_number(12345))

