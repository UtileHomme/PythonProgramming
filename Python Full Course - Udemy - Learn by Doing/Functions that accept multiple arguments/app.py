def add_all(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4


vals = {'a1': 1, 'a2': 3, 'a3': 4, 'a4': 5}

sum = add_all(**vals)

print(sum)


def add_all(*args):
    print(args)


add_all(5, 7, 6, 7)


def add_all1(*args):
    return sum(args)

# Positional Arguments
print(add_all1(5, 7, 4, 4))

# kwargs is a dictionary
def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print(f'For {k} we have {v}.')

pretty_print(username='jatin', access_level='admin')

# Named arguments
pretty_print(**{'username':'jatin', 'access_level':'admin'})

