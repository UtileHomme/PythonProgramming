import functools

user = {
    'username': 'jose123',
    'access_level': 'admin'
}



def user_has_permission(func):
    # Wrapping around the secure function so as to retain the name of the functions
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    return 'Password for {panel} panel is 1234'

@user_has_permission
def another():
    return 'hello'


# This is no longer required
# my_secure_function = user_has_permission(my_function)

print(my_function.__name__)

print(my_function('movies'))




