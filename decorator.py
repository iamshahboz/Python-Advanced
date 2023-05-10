# It is something which allows you to add functionality to existing object without
# modification. We have class decorators and function decorators.
# In other words, decorator is a function that takes another function as argument and extends
# its behavoir of this function without modification

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args,**kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add_five(x):
    return x+5
    

result = add_five(10)
print(result)






