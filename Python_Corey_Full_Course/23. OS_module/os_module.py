import os

from datetime import datetime

# gives all the attributes and methods that we have access to in this module
print(dir(os))

# Gives the current working directory
print(os.getcwd())

# Changes the directory to the one that we want
# os.chdir('/')

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
# os.rmdir('OS_demo_2')
# os.removedirs('OS_demo_2/Sub_dir_1')

# How to find the directories in the current working directory
print(os.listdir())

# How to rename a file or folder
# os.rename('test.txt', 'demo.txt')

# How to print all information about a file
# print(os.stat('pagefile.sys'))

# How to find the size of a file
# mod_time = os.stat('pagefile.sys').st_mtime

# How to convert timestamp into datetime
# print(datetime.fromtimestamp(mod_time))

# How to print all files and directories in a folder

# for dirpath, dirnames, filenames in os.walk(r'C:\Users\pksk6\OneDrive\Youtube Learning Videos\Python\Python Programming by Corey'):
#     print('Current path', dirpath)
#     print('Directories', dirnames)
#     print('Files' , filenames)
#     print()

# How to get environment variables
print(os.environ.get('HOME'))

# How to define a new file path
file_path = os.path.join(r'C:\Users\pksk6\OneDrive', 'test.txt')
print(file_path)

# Gives the base name of the entire path
print(os.path.basename('tmp/text.txt'))

# Gives the directory name of the entire path
print(os.path.dirname('tmp/text.txt'))

# Gives the directory and name of the entire path
print(os.path.split('tmp/text.txt'))

# How to check the existence of a path
print(os.path.exists('tmp/text.txt'))

# How to check if a path is a directory
print(os.path.isdir('tmp/text.txt'))

# How to check if a path is a file
print(os.path.isfile('tmp/text.txt'))

# How to get the extension of the file
print(os.path.splitext('tmp/text.txt'))

# How to fetch the modules available in os.path module
print(dir(os.path))
print()






