age = 20

def increase_age(current_age):
    current_age = current_age + 1

# 1762225824
print(id(age))

increase_age(age)

# 1762225824
print(id(age))