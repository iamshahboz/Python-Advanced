'''
Itertools module is a collection of tools for handling iterators. Simply put iterators
are data types that can be used in a for loop

from itertools import product,permutations

a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))
'''
from itertools import permutations, combinations
num = [1,2,3]
perm = permutations(num)
print(list(perm)) #this will return all possible combinations of three digits


