import numpy

# Question 3
# Compute the sum of the diagonal element of a given array/
vec = numpy.array([[0, 1, 2],
                   [3, 4, 5]])

vec_sum = numpy.trace(vec)
print(f"Sum: {vec_sum}")
