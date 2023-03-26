'''
#sets: unordered, mutable, no duplicates
myset = {2,5,9,12,2,9,0,9}
print(myset)
# as you see duplicates are not allowed

another_set = set("Hello world")
print(another_set)

#if you want to have an empty set
my_set = set()

#set is mutable and you can add elements using add method
my_set.add(5)
my_set.add(12)
my_set.add(20)
print(my_set)

#you can remove the element as well: remove and discard
# clear method will empty our set
#pop method will return the element and remove it from the set


my_set.remove(20)
print(my_set)

# we can iterate over set
for i in my_set:
    print(i)


if 120 in my_set:
    print("Yes")

print("No")

odds = {3,11,9,17,21}
even = {6,10,2,14,20}
primes = {2,3,5,7}

u = odds.union(even)
#this will combine two sets without duplications
print(u)

'''
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

#the difference will return a set with all elements from the first set that
#are not in the second set
# diff = setB.difference(setA)
# print(diff)

#this will add the elements of setB to set A which is not there, without any duplicate
setA.update(setB)
print(setA)







