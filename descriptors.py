'''
Descriptors are specific python feature that power a lot of magic hidden under the language
hood

Descriptor are python objects that implement a method of descriptor protocol
which gives you the ability to create   objects that have special behavior
when they are accessed as attributes of other objects. Here you can see
the corrent definition of the descriptor protocol
'''

'''
__get__(self, obj, type=None) -> object # non data descriptor

__set__(self, obj, value) -> None # data descriptor

__delete__(self, obj) -> None 

__set_name__(self, owner, name)
'''
# class Verbose_attribute():
#     def __get__(self,obj, type=None) -> object: 
#         print('Accessing the attribute to get the value')
#         return 42 
#     def __set__(self,obj, value) -> None:
#         print('accessing the attribute to set the value ')
#         raise AttributeError('Can not change the value')
    
# class Foo():
#     attribute1 = Verbose_attribute()

# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)

# How attributes are accessed with the lookup chain

# class Vehicle():
#     can_fly = False 
#     number_of_wheels = 0

# class Car(Vehicle):
#     number_of_wheels = 4

#     def __init__(self,color):
#         self.color = color

# my_car = Car('red')
# print(my_car.__dict__)
# print(type(my_car).__dict__)

my_tuple = [2,5,7,9,12,99]

print(dir(my_tuple))




