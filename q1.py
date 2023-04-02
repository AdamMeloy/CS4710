import numpy

# Question 1
# Using NumPy, create random vector of size 15 having only Integers in the range 1-20

#   1. Reshape the array to 3 by 5
#   2. Print array shape.
#   3. Replace the max in each row by 0

# create random vector
vec = numpy.random.randint(1, 20, 15)
print(f"Random Array\n{vec}\n")

# reshape to 3 x 5
vec = numpy.reshape(vec, (3, 5))
print(f"Reshaped Array\n{vec}\n")

# gets a list of the indexes for the highest numbers
max_idx = numpy.argmax(vec, axis=1).tolist()
# replaces the highest numbers with 0
for idx in max_idx:
    vec[max_idx.index(idx)][idx] = 0
print(f"Max Values Removed\n{vec}\n")

# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements)
vec2 = numpy.array([[48, 44, 40, 36], [32, 28, 24, 20], [16, 12, 8, 4]], numpy.int32)
# also print the shape, type and data type of the array
print(f"4-Byte Integer Array\n{vec2}\nType: {type(vec2)}\nData Type: {type(vec2[0][0])}")
