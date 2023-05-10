'''Python comes with different built in modules to generate random numbers'''
# sudo random
import random 

# this will generate random float between 0 and 1
number = random.random()
print(number)
# you can also give a range
number = random.uniform(1,10)
print(number)

# if you want to have integers you can do
number = random.randint(10,50) # note that upper bound will be included
number = random.randrange(10,50) # this way upper bound is not included

my_list = list("ABCDEFGHIJK")
a = random.choice(my_list) # this will take one random element
print(a)

a = random.sample(my_list,3) # this will take three elements(unique)

a = random.choices(my_list,key=3) # this will take elemements(but can be duplicated)








