def function_1(name, age, rollno):
    print("The name of the student is", name, " and age is ", age, " rollno is ", rollno)


function_1("Harry", 22, 344)


# *args takes variable number of arguments and gives the arguments as a tuple
def function2(*args):
    type(args)
    if len(args) == 3:
        print("The name of the student is", args[0], " and age is ", args[1], " rollno is ", args[2])
    else:
        print("The name of the student is", args[0], " and age is ", args[1])

function2("Harry", 22)

listName = ["Harry", 22, 5]

function2(*listName)

marklist = {
    "Jatin" : 100,
    "Jatin2" : 89,
    "Jatin3" : 23
}

#kwargs have key value pairs
def printmarks(**kwargs):
    type(kwargs)
    for key,value in kwargs.items():
        print(key, value)


printmarks(**marklist)





