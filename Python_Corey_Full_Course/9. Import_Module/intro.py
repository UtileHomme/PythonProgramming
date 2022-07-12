# import my_module

# In case the module to be imported is not in the same file path as project, we can add the module folder path to sys
import math
import sys
import random
import datetime, calendar, os, antigravity

sys.path.append('module full path')

# Above method is not preferred. Better approach is to add the Module folder path to the Python Environment variables path

from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

# List of paths where Python looks for modules to be imported
# print(sys.path)

# How to pick a random value from a list
random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)

print(math.sin(rads))

# Getting todays data
todays_date = datetime.date.today()
print(todays_date)

# Getting whether year is leap year
print(calendar.isleap(2020))

# getting the current working directory
print(os.getcwd())

# This will give a os.py library file location
print(os.__file__)
