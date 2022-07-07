users = ['a', 'b', 'c', 'd']
computer = ['dd', 'cc', 'dd', 'gd']

for i in range(0, len(users)):
    template = "Computer used by {0} is {1}"
    print(template.format(users[i], computer[i]))
