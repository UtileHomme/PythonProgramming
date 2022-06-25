tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = set()

for tag in tags:
    lowercase_tags.add(tag.lower())

print(lowercase_tags)

# Using map and lambda

lowercase_tags1 = set(map(lambda tag: tag.lower(), tags))

print(lowercase_tags1)

# Using set comprehensions

lowercase_tags2 = {tag.lower() for tag in tags}

print(lowercase_tags2)

# Using set comprehensions with if

new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

print(new_tags)
