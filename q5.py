import math

# Question 5
# The radius of a circle is 30 meters.
radius = 30
print(f"Radius: {radius}")

# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
_area_of_circle_ = math.pi * pow(radius, 2)
print(f"Area: {_area_of_circle_}")

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * math.pi * radius
print(f"Circumference: {_circum_of_circle_}\n")

# Take radius as user input and calculate the area.
radius = int(input("Enter radius: "))
_area_of_circle_ = math.pi * pow(radius, 2)
print(f"Area: {_area_of_circle_}\n")