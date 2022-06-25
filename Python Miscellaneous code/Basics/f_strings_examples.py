name = 'John'

s = F'Hello, {name.upper()} !'
print(s)

# Formatting numbers using f strings
previous = 99.2
current = 110.3

vs_previous = (current - previous) /previous

# {[number]:[previous][type]
print(f'{vs_previous:.2%}')