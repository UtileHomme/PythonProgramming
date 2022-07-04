import functools

user = {
    'username': 'jose123',
    'access_level': 'admin'
}


# this is a decorator
def third_level(access_level):
    def user_has_permission(func):
        # Wrapping around the secure function so as to retain the name of the functions
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == 'admin':
                return func(panel)
        return secure_func
    return user_has_permission



# We are dynamically adding the parameter value for access level
@third_level('admin')
def my_function(panel):
    return 'Password for {panel} panel is 1234'


# This is no longer required
# my_secure_function = user_has_permission(my_function)

print(my_function.__name__)

print(my_function('movies'))

# user_has_permission = third_level('admin')
# my_function = user_has_permission(my_function)

# The below function can be divided into the above two lines
my_function = third_level('admin')(my_function)



