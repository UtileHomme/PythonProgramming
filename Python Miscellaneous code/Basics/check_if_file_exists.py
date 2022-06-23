# 1. Using os.path.exists() function

from os.path import exists


path_to_file = 'readme2.txt'
file_exists = exists(path_to_file)

print(file_exists)

# 2. Using path lib module

from pathlib import Path

from pathlib import Path

path = Path('readme2.txt')

print(path.is_file())


