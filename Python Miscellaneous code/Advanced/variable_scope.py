counter = 10


def reset():
    counter = 0
    print(counter)

reset()
print(counter)

# The global keyword will allow us to use the value of counter defined outside the reset function and modify it

counter = 10


def reset():
    # This is not a good practice though. Better to define a new variable
    global counter
    counter = 0
    print(counter) # 0


reset()

print(counter) # 0

