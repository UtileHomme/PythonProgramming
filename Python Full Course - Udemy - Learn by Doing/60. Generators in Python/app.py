def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i = i + 1


# Generator remembers the last value of i after yield
generatorValue = hundred_numbers()
print(next(generatorValue))
print(next(generatorValue))
print(list(generatorValue))
