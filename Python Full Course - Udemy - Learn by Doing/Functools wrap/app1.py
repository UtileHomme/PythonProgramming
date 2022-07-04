import functools

user = {
    'username': 'jose123',
    'access_level': 'admin1'
}


# this is a decorator
def user_has_permission(func):

    # Wrapping around the secure function so as to retain the name of the functions
    @functools.wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func

@user_has_permission
def my_function():
    return 'Password for admin panel is 1234'

@user_has_permission
def another():
    pass

# This is no longer requred
# my_secure_function = user_has_permission(my_function)

print(my_function())
print(my_function.__name__)
print(another.__name__)


