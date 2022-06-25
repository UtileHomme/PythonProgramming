a = 100
b = a

result = a is b

# True because both reference the same object
print(result)

c = 100
d = 100

result1 = c is d

# True because both are still pointing to same object
print(result1)

# However for lists which are mutable, this is different

ranks = [1,2,3]
ratings = [1,2,3]

# False because lists are mutable and are considered different here
print(ranks is ratings)


# is vs == operator

a = 100

b = a

# True
print(a==b)

# True
print(a is b)

# However for lists, results will be different

ranks = [1,2,3]
ratings = [1,2,3]

# False because lists are mutable and are considered different here
print(ranks is ratings)

# True becuase the elements in the lists are same
print(ranks == ratings)