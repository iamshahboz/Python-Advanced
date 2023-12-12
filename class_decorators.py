# Here are top 10 built in class decorators that optimize the python code 


# 1. @classmethod

# class GFGClass:
#     class_var = 10 

#     @classmethod
#     def gfg_class_method(cls):
#         print('This is class method')
#         print(f' Value of the class variable {cls.class_var}')
    


# GFGClass.gfg_class_method()


# 2. @abstractmethod

'''It is a class that can not be instanciated. It can be subclass for any other class
ABC class stands for Abstract Base Class'''

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass 

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side 

#     def area(self):
#         return self.side ** 2
    
# square = Square(10)
# print(square.area())


# staticmethod

'''Static methods are simply utility methods that are not bound to a class or an instance
of the class. The @staticmethod is built-in decorator that is used to create a static method'''


# class GFGClass:

#     @staticmethod
#     def gfg_static_method():
#         print('This is static method')

# GFGClass.gfg_static_method()


# atexit 

'''The atexit.register decorator is used to call the function when the program is exiting.
The functionality  is provided by alexit module. This function can be used to perform
to clean-up tasks before the program exits.

'''

import atexit

@atexit.register
def gfg_exit_handler():
    print('Bye, Geeks!')

print('Hello Geeks')




