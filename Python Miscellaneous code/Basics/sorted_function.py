# Sort function modifies the original list

# Sorted function doesn't modify the original list. Instead it returns a new list

guests = ['James', 'Mary', 'John', 'Patricia']

sorted_guest = sorted(guests)

print(sorted_guest)

reverse_sorted_guests = sorted(guests, reverse=True)

print(reverse_sorted_guests)