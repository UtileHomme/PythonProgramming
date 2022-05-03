# Old Way

numbers = [0,1,2,3,4]

doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

# By using list comprehensions
doubled_numbers1 = [number * 2 for number in numbers]
print(doubled_numbers1)

doubled_numbers2 = [number * 2 for number in range(5)]
print(doubled_numbers2)
