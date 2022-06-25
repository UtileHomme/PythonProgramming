s1 = {'a', 'b'}
s2 = {'c', 'b'}

s3 = s1.union(s2)

print(s3)

# Another way

s4 = s1 | s2
print(s4)

# Union can be performed between lists and sets also

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)

# But | operand can only be used for sets

ratings1 = rates | ranks

print(ratings1)
