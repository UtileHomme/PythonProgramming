import os

# gives all the attributes and methods that we have access to in this module
print(dir(os))

# Gives the current working directory
print(os.getcwd())

# Changes the directory to the one that we want
os.chdir('/')

# Gives the current working directory after changing directory
print(os.getcwd())

# How to find the directories in the current working directory
print(os.listdir())

# How to create a new directory
# os.mkdir('OS_demo_2')
# os.makedirs('OS_demo_2/Sub_dir_1')

# How to find the directories in the current working directory
print(os.listdir())

# How to delete the folders
os.rmdir('OS_demo_2')
os.removedirs('OS_demo_2/Sub_dir_1')


