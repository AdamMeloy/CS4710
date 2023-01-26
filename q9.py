# Question 9
# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

# get user input
pounds = [int(i) for i in input("Provide a list of weights in pounds for a group of students: ").split(",")]

# convert weight to kg
kilograms = []
for item in pounds:
    # round to proper precision
    new_item = round((item / 2.205), 2)
    kilograms.append(new_item)

print(kilograms)