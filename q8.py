# Question 8
# Use the string formatting method to display the following:
# “The area of a circle with radius 10 is 314 meters square.”
radius = 10
area = 3.14 * radius ** 2

result = 'The area of circle with radius {} is {} meters square.'.format(radius, int(area))
print(result)