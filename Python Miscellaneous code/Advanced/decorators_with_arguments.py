# To call the say function 5 times we can use a decorator in the following way

from functools import wraps

def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result

    return wrapper


@repeat
def say(message):
    ''' print the message
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')

# But the above code hardcodes the number of times as 5. Alternatively, we can
# take times parameter as an argument in the decorator

from functools import wraps


def repeat(times):
    ''' call a function a number of times '''
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat(10)
def say(message):
    ''' print the message
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')
