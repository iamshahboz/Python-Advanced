'''Generators are functions that return an object that can be iterated over
And the special thing is that, they generate the items inside the object lazily
which means they gererate the items only one at a time and only when you ask for it.
They are memory efficient. They are written like normal function but instead of return 
yield is used
import sys


def my_generator():
    yield 1
    yield 2
    yield 3 

g = my_generator()
value  = next(g)
print(value)

for i in g: 

    print(i)

def countdown(num):
    print("Starting...")
    while num > 0:
        yield num 
        num -=1

cd = countdown(4)
value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

# Generator will save a lot of memory when you work with large data


'''
# Lets say we want a function which takes number as imput and it returns
# a sequence starting from 0 all the way up to that number
import sys
def firstn(n):
    nums = []
    num = 0
    while num<n:
        nums.append(num)
        num +=1
    return nums 

print(sys.getsizeof(firstn(20000)))

# with this way, all the numbers are stored in this list
# You can use generator instead

def firstn_generator(n):
    num = 0
    while num<n:
        yield num
        num += 1

print(sys.getsizeof(firstn_generator(20000)))

# you can analyze this, and you can see huge difference








