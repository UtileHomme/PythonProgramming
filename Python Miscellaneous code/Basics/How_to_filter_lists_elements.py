scores = [3,22,55,21,77,25]

filtered = []

for score in scores:
    if score >= 25:
        filtered.append(score)

print(filtered)

# Simulating the above logic with filter() function

# filtered is an iterator
filtered = filter(lambda score: score >= 25, scores)

print(list(filtered))

# Another example

countries = [
    ['China', 123],
    ['United States', 235],
    ['India', 532],
    ['Brazil', 6743]
]

populated = filter(lambda c: c[1] <1000, countries)

print(list(populated))
