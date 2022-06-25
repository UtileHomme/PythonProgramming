import ctypes

counter = 100

# Id function finds the memory address of the variable
print(id(counter))

# to convert memory address to hexademical
print(hex(id(counter)))

# Reference counting

max = counter

print(id(max))

max = 999

print(id(max))

# How to identify number of references to a particular memory address

# use ctypes.c_long.from_address(address).value

def ref_count(address):
    return ctypes.c_long.from_address(address).value

numbers = [1,2,3]

numbers_id = id(numbers)

# 1 reference
print(ref_count(numbers_id))

ranks = numbers

# 2 references because rank is also pointing to same address
print(ref_count(numbers_id))

ranks = None

print(ref_count(numbers_id))

