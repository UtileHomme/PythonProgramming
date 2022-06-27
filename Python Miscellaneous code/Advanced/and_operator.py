# if b:
#     c = a / b
# else:
#     c = b

a = 10
b = 0

# If b = 0 which is false, no need to go to a/b
c = b and a / b
print(c)

a = 10
b = 5

# since b >0, go and evaluate a / b
c = b and a / b
print(c)


# More examples

def avg(*numbers):
    total = sum(numbers)
    n = len(numbers)
    if n > 0:
        return total / n
    return 0


if __name__ == "__main__":
    print(avg())


# Another way of doing this

def avg(*numbers):
    total = sum(numbers)
    n = len(numbers)
    return n and total / n


if __name__ == "__main__":
    print(avg(1, 2, 3))
