import numpy
from numpy import linalg

# Question 2
# Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
sq_arr = numpy.array([[3, -2],
                     [1, 0]])

# computes eigenvalues and right eigenvectors
res = linalg.eig(sq_arr)

print(f"Eigenvalues: {res[0]}\nRight Eigenvectors: {res[1]}")
