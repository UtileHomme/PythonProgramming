try:
    pass
    # code that you want to protect from exceptions
except Exception as ex:
    pass
    # code that handle the exception
finally:
    pass
    # code that always execute whether the exception occurred or not
# else:
#     print('hello')
# code that excutes if try execute normally (an except clause must be present)

# CORRECT WAY TO HANDLE EXCEPTIONS
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError('The second argument (b) must not be zero')

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
else:
    print('result:', result)

# When you catch an exception in the except clause, you need to place the exceptions from most specific to the least specific in terms of exception hierarchy.

colors = ['red', 'green', 'blue']
try:
    print(colors[3])
except IndexError as e:
    print(type(e), 'Index error')
except LookupError as e:
    print(type(e), 'Lookup error')

