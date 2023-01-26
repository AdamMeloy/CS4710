# Question 1
# Sort the list and
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

# find the min and max age
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.insert(len(ages), min_age)
ages.insert(len(ages), max_age)

# Find the median age (one middle item or two middle items divided by two)
med_age = (ages[4] + ages[5])/2

# Find the range of the ages (max minus min)
ran_age = max_age - min_age

# Find the average age (sum of all items divided by their number)
avg_age = 0
for item in ages:
    avg_age += item

avg_age /= 10

print(f"Maximum Age: {max_age}\n"
      f"Minimum Age: {min_age}\n"
      f"Median Age: {med_age}\n"
      f"Average Age: {avg_age}\n"
      f"Range of Ages: {ran_age}")