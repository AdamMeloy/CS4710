# Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(f"IT Companies Length: {len(it_companies)}")

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(f"IT Companies: {it_companies}")

# Insert multiple IT companies at once to the set it_companies
it_companies.update({"Facebook 2", "Google 2"})
print(f"IT Companies: {it_companies}")

# Remove one of the companies from the set it_companies
it_companies.remove("Google 2")
print(f"IT Companies: {it_companies}")

# What is the difference between remove and discard
# remove will provide a keyError if it does not remove an item,
# discard will do nothing

# Join A and B
print(f"AB Union: {A.union(B)}")

# Find A intersection B
print(f"AB Intersection: {A.intersection(B)}")

# Is A subset of B
print(f"Is A subset of B? {B.issubset(A)}")

# Are A and B disjoint sets
print(f"Are A and B disjoint sets? {A.isdisjoint(B)}")

# Join A with B and B with A
C = A.union(B)
D = B.union(A)

# What is the symmetric difference between A and B
print(f"Symmetric Difference of A and B: {C.symmetric_difference(D)}")

# Delete the sets completely
A.clear()
B.clear()

# Convert the ages to a set and compare the length of the list and the set.
lage = list(age)
print(f"List Length: {len(lage)}\n"
      f"Set Length: {len(age)}")