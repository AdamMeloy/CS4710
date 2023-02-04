# Write a function that accepts a string and calculate the number of upper-case letters and lower-case letters.

# Expected Output:
# No. of Upper-case characters: 3
# No. of Lower-case Characters: 12


def char_count(input_string):
    # ints for holding char counts
    upper_count = 0
    lower_count = 0

    for char in input_string:
        # check if char is uppercase
        if char.isupper():
            upper_count += 1
        # check if char is lowercase
        elif char.islower():
            lower_count += 1

        # remove char from string
        input_string.replace(char, "")

    # print char counts
    print(f"No. of Upper-case characters: {upper_count}")
    print(f"No. of Lower-case characters: {lower_count}")


if __name__ == '__main__':
    inp = 'The quick Brow Fox'
    char_count(inp)