# If we don't enter a language it will default to Python value
lang = input('Enter your language:') or 'Python'
print(lang)

# Another example

def get_data(args=None):
    if args:
        return [1, 2, 3]
    return []


lowest = min(get_data(args=True))
print(lowest)

# This will give an error
# lowest = min(get_data())
# print(lowest)

# To resolve the above

def get_data(args=None):
    if args:
        return [1, 2, 3]
    return []


lowest = min(get_data() or [0])
print(lowest)

