# If doc directory doesn't exist
try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create a new file')
except FileNotFoundError:
    print("The 'docs' directory doesn't exist")

# If you want to avoid creating a new file which already exists, mode should be 'x'
with open('readme2.txt', 'x') as f:
    f. write('No need to create a file')