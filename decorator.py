# It is something which allows you to add functionality to existing object without
# modification. We have class decorators and function decorators.
# In other words, decorator is a function that takes another function as argument and extends
# its behavoir of this function without modification

# def start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def add_five(x):
#     return x+5
    

# result = add_five(10)
# print(result)




# # functions
# def add_one(number):
#     return number + 1 

# print(add_one(4))

# first class objects

# def say_hello(name):
#     return f'Hello {name}'

# print(say_hello('Kirill'))


# def be_awesome(name):
#     return f'Yo {name}, together we are awesomest'

# print(be_awesome('Garry'))


# def greet_bob(greeter_func):
#     return greeter_func('Yalla')


# print(greet_bob(say_hello))


## inner functions

# def parent():
#     print('Printing from parent function() ')

#     def first_child():
#         print('Printing from first child_function()')

#     def second_child():
#         print('Printing from the second child function() ')

#     second_child()
#     first_child()

# parent()

## Returning functions from functions

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
    
#     def second_child():
#         return "Call me Liam"
    
#     if num == 1:
#         return first_child
#     else:
#         return second_child

# print(parent(1))

# simple decorators 

# def my_decorator(func):
#     def wrapper():
#         print('Something is happening before the function is called')
#         func()
#         print('Somethind is happening after the function is called')
#     return wrapper 

# def say_wee():
#     print('Whee!')

# say_wee = my_decorator(say_wee)

# say_wee()

# another example 
# from datetime import datetime 

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <=datetime.now().hour < 22:
#             func()
#         else:
#             pass 
#     return wrapper

# def say_wee():
#     print('Say whee')


# say_wee = not_during_the_night(say_wee)

# say_wee()

# few real world examples of decorators 

# import functools 

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         print('Do something before')
#         value = func(*args, **kwargs)
#         print('Do something after')
#         return value
#     return wrapper_decorator


# @decorator
# def my_func():
#     print('Yoo')

# my_func()

'''
import functools 
import time 

def timer(func):
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f' Finished {func.__name__!r} in {run_time:.4f} seconds')
        return value 
    return timer_wrapper 

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(3887)
'''
import functools 
import time 

def slow_down(func):
    # Sleep for one seconds 
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Time is finished')
    else:
        print(from_number)
        countdown(from_number - 1)
         

countdown(11)
































