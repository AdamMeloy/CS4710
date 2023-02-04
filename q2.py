# Output list items in odd indices

# Expected Output
# 20, 40, 60, 80, 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    # check if index is odd
    if (i % 2) != 0:
        print(my_list[i], end=", ")