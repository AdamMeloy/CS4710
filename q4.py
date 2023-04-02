import numpy

# Question 4
# Write a NumPy program to create a new shape to an array without changing its data.
# Example Result:
# [[1 2 3]
# [ 4 5 6]]

# create array
vec1 = numpy.array([[1, 2],
                    [3, 4],
                    [5, 6]])

# create new array from data
vec2 = numpy.reshape(vec1, (2, 3))
print(vec2)
