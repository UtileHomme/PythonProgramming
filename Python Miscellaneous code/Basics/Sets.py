#1. Defining a set
skills = {'a', 'b', 'c'}

#2. Defining an empty set

empty_set = set()

#3. Passing a list as an iterable to a set

skillsSet = set(['Problem solving', 'Critical Thinking'])

print(skillsSet)

#4. How to check if an element is in a set

ratings = {1,2,3,4,5}

rating = 1

if rating in ratings:
    print(f'The set contains {rating}')

#5. How to add an element to a set

skillsSet1 = {'a', 'b'}

skillsSet1.add('c')

print(skillsSet1)

#6. how to remove an element from a set

skills1 = {'a', 'b', 'c', 'd'}

# This removes a from the set
skills1.remove('a')

# This raises a Key error because c doesn't exist in skills1
# skills1.remove('c')

# To avoid above, use discard function
skills1.discard('c')

# 7. How to return an element from a set

skill = skills1.pop()

print(skill, skills1)

# 8. Removing all elements from a set

skills1.clear()

print(skills1)

# 9. To get an immutable set (which cannot be modified) from an existing set (which can be modified)

skills = {'t', 'w', 'y'}

skillsfrozen = frozenset(skills)

print(skillsfrozen)

# 10. How to loop through a set

for skilled in skills:
    print(skilled)

# 11. How to get index of the elements in a set

for index, skilled in enumerate(skills):
    print(f"{index}. {skilled}")

print("\n")

# 12. How to start the index at a customized index

for index, skilled in enumerate(skills, 2):
    print(f"{index}. {skilled}")



