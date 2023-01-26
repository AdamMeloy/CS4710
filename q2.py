# Question 2
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": None,
    "color": None,
    "breed": None,
    "legs": None,
    "age": None
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
    "first_name": None,
    "last_name": None,
    "gender": None,
    "age": None,
    "marital_status": None,
    "skills": [None],
    "country": None,
    "city": None,
    "address": None
}

# Get the length of the student dictionary
print(f"Student Length: {len(student)}")

# Get the value of skills and check the data type, it should be a list
print(f"Skills Type: {type(student['skills'])}")

# Modify the skills values by adding one or two skills
student["skills"] = ["Programming", "Commenting"]

# Get the dictionary keys as a list
# Get the dictionary values as a list
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")