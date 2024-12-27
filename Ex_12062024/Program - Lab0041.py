# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# given numerical score (e.g., A ,B ,C ,D , or F)
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# MULTIPLE CONDITION If, elif, else

# Step 1 - Logic Building
# input?
score = int(input("Enter the score\n: "))  # 89
# output? - string - A,B,C,D,F -str

# Step 2
# Write a rough logic and convert to real one


# score >=90 and score<=100 -> A
# score >=80 and score<=89 -> B
# score >=70 and score<=79 -> C
# score >=60 and score<=69 -> D
# score >=0 and score<=59 ->  F


if score >= 90 and score <= 100:
    print(" Your Grade is A")
elif score >= 80 and score <= 89:
    print(" Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
elif score >= 0 and score <= 59:
    print("Your Grade is F")
else:
    print("Invalid score")
