# Write a function that takes a list and returns a new list with unique items of the first list.

# Expected Output:
# [1, 2, 3, 4, 5]


def make_unique(input_list):
    # create new list
    unique_list = []

    for item in input_list:
        # check if item is already in list
        if item not in unique_list:
            unique_list.append(item)

    # return list
    return unique_list


if __name__ == '__main__':
    sample = [1, 2, 3, 3, 3, 3, 4, 5]
    sample = make_unique(sample)
    print(sample)