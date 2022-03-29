# Opening a file for reading
my_file = open('data.txt', 'r')

file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name:')

# For writing - this will overwrite the existing file
my_file_writing = open('data.txt', 'w')

my_file_writing.write(user_name)

my_file_writing.close()







