numbers = [4,27,2,77,22]

print(numbers[-2])

# 1. Modifying elements in a list

numbers[1] = 78

print(numbers)

# 2. Adding elements to a list

numbers.append(654)

print(numbers)

# 3. Adding elements to a list at a particular position

numbers.insert(4,1234)

print(numbers)

# 4. Removing elements from a list

del numbers[0]

print(numbers)

# 5. Removing last element from list and getting its value

last = numbers.pop()

print(last, numbers)

#6. Removing element using index

second = numbers.pop(1)

print(second, numbers)

# 7. Removing element using value of element

numbers.remove(1234)

print(numbers)