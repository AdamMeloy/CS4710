# Write code that appends the type of elements from a given list.

# Expected Output
# [23, 'Python', 23.98]
# [<class 'int'>, <class 'str'>, <class 'float'>]

x = [23, 'Python', 23.98]

# print items in list
print(x)

# print types of items in list
print(f"{[type(item) for item in x]}")