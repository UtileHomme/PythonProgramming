# kwargs is for unpacking arguments in the form of a dictionary or for passing a dictionary

def connect(**config):
    print(config)

config = {
    'server' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'jatin'
}

connect(**config)

# how to use args and kwargs together

# args is used for unpacking into a tuple

def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn(1,2,x = 10, y = 20)