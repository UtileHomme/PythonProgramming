# Try not to use tuple of grades because it is difficult to add new values
# Set of Grades also should not be used because of non-duplicacy
grades = [80, 75, 90, 100]

total = sum(grades)

length = len(grades)

avg = total / length
print(avg)