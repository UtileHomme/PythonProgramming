# write is using for adding a single string
with open('readme.txt', 'w') as f:
    f.write('readme')

lines = ['Readme', 'How to write test files']

with open('readme1.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# writelines is used for adding a list, tuple, set of strings. This doesn't add a new line automatically
with open('readme2.txt', 'w') as f:
        f.writelines(lines)

# writelines is used for adding a list, tuple, set of strings. This add a new line automatically
with open('readme3.txt', 'w') as f:
        f.writelines('\n'.join(lines))




