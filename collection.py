'''The collections module implements special container data types and provides alternatives
with some additional functionality compare to the general built in containers 
like dictionaries, lists or tuples.
We will see five different types from the collections module
Counter, namedtuple, OrderedDict, defaultDict, deque

'''
# Counter
# note: dont name the file name as collections, you will get an error
# It is a container that stores the elements as dictionary keys  and their counts as dict values
'''
from collections import Counter
a = "aaaaaabbbccc"
my_counter = Counter(a)
print(my_counter.values())

# to get the most common element(type)
# 1 in the bracket mean I want to only one most common type
print(my_counter.most_common(2))

# to get the list with all different elements 
print(list(my_counter.elements()))

# Named tuple
from collections import namedtuple
# it is an easy to create lightweight object type

Point = namedtuple("Point","x,y")
pt = Point(2,4)
print(pt)

# you can access the fields
print(pt.x,pt.y)

'''
#from collections import OrderedDict
#Ordered dict is just like regular dictionaries but they remember the order the items were inserted
# don't use it, because after python 3.7 regular dict remember the order

#default dict
from collections import defaultdict
# it is similar to usual dict container, only difference it will have a default value
# if the key is not set
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])


# deque
# the deque is double ended queue, it can be used to add or remove elements from both ends
from collections import deque
d = deque()

d.append(4)
d.append(7)
d.append(12)
# this will add element from the leftside
d.appendleft(30)
# this removes the element from the leftside
d.popleft()
print(d)

# if can add several items to the deque at one time
d.extend([10,5,-5])
print(d)

# extendleft will add element at leftside







