def square_numbers(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

my_nums = square_numbers([1, 2, 3, 4, 5])

for i in my_nums:
    print(i)

# Another way of doing  the above

my_nums = (x * x for x in [1, 2, 3, 4, 5])

print()
for num in my_nums:
    print(num)

print()
print(list(my_nums))

# [1, 4, 9, 16, 25]
