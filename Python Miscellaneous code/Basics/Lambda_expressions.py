# 1. Function that accepts a function eg. - THE CONVENTIONAL WAY

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


def first_last_formatter(first_name, last_name):
    return f"{first_name} {last_name}"


def last_fast_formatter(first_name, last_name):
    return f"{last_name} {first_name}"


full_name = get_full_name('John', 'Doe', first_last_formatter)

print(full_name)

full_name = get_full_name('John', 'Doe', last_fast_formatter)

print(full_name)


# 2. Function that accepts a function eg. - THE LAMBDA WAY

# Lambda convention - lambda parameters : expression

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name_lambda = get_full_name('John', 'Doe', lambda first_name, last_name: f"{first_name} {last_name}")

print(full_name_lambda)

full_name_lambda = get_full_name('John', 'Doe', lambda first_name, last_name: f"{last_name} {first_name}")

print(full_name_lambda)
