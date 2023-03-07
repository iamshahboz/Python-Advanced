'''
my_tuple = tuple(["Toronto","Eddy","Boston"])
print(my_tuple)

my_tuple = ("Max",28,"Boston")
print(my_tuple)

#if you have one element in tuple you should put comma after it, otherwise it is str

second_tuple = ("Sony",)
print(type(second_tuple))

#tuple is not mutable so you can not assign the value to something
#my_tuple[0] = "Robert"

# we can iterate over
for i in my_tuple:
    print(i)


if "Ontario" in my_tuple:
    print("Yes")
else:
    print("No")

my_tuple = ('a','j','k','u','r','f','c','v','a','n','l')
#print(my_tuple.count('a')) #to get the number of accuran

print(my_tuple.index('k'))
#to get the index of the first occurance

a = (2,4,5,1,7,8,0,12,4,6,75)
b = a[:5:2]
print(b)



#you can do unpacking, note that the number of elements should match
my_tuple = ("Max",28,"Boston")
name,age,city = my_tuple
print(name,age,city)

my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple
print(i1)
print(i2) #for this case i2 is the list of elements in between
print(i3)
'''












