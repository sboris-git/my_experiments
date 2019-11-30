# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('original display func ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with args ({},{})'.format(name, age))

display_info('John', 25)
display()


#
# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('wrapper executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @decorator_class
# def display():
#     print('original display func ran')
#
# @decorator_class
# def display_info(name, age):
#     print('display_info ran with args ({},{})'.format(name, age))
#
# display_info('John', 25)
# display()


# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function
#
# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
#
# hi_func()
# bye_func()

'''
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
'''
