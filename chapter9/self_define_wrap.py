from functools import wraps, partial
import logging
# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


import logging
logging.basicConfig(level=logging.DEBUG)
print(f'add result: {add(3, 5)}')
add.set_message('Add called')
print(f'add result: {add(3, 5)}')
add.set_level(logging.WARNING)
print(f'add result: {add(3, 5)}')


import time
def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name: {func.__name__},time use: {end - start} s')
        return result
    return wrapper

@time_use
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)
countdown.set_level(logging.WARNING)
countdown.set_message("Counting down to zero")
countdown(10000000)


@logged(logging.DEBUG)
@time_use
def countdown(n):
    while n > 0:
        n -= 1


# @attach_wrapper(wrapper)
# def get_level():
#     return level
#
# # Alternative
# wrapper.get_level = lambda: level
#
#
# @wraps(func)
# def wrapper(*args, **kwargs):
#     wrapper.log.log(wrapper.level, wrapper.logmsg)
#     return func(*args, **kwargs)
#
# # Attach adjustable attributes
# wrapper.level = level
# wrapper.logmsg = logmsg
# wrapper.log = log