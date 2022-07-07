try:
    print("I will try this code for exception")
    # open("this.txt")
except Exception as e:
    print(e)
else:
    print("This will execute only if there is NO exception")
# finally will run whether an exception occurs or not
finally:
    print("This will be printed irrespective of the exception occurrence")

