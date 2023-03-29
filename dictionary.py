# Dictionary is collection data type which is Unordered and Mutable
# It consists of a collection of key value pairs. Each key value pairs maps the key to the 
# associated value

#my_dict = {"name":"Max","age":28,"city":"New York"}
#print(my_dict)
'''
# we can also use the dict function, we put the keys as arguments
my_dict2 = dict(name="Tommy",age=20,city="Hamburg")
print(my_dict2) 

#when you want to access the values you can do
value = my_dict2['name']
print(value)

#you can add key value pair 
my_dict2["email"] = "tommy@post.com"
print(my_dict2)

#if we want to delete items we have several options

#del(my_dict2['name'])
#print(my_dict2)

if "name" in my_dict2:
    print(my_dict2['name'])

# you can use try except for that as well
try:
    print(my_dict2['last_name'])
except:
    print("This key does not ")

# you can loop through dictionary

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)
   
# To get only keys or values you can do
print(my_dict.keys())
print(my_dict.values())
    

# you can combine both of them

for key,value in my_dict.items():
    print(key,value)

# to copy the dictionary
my_dict_copy = my_dict
print(my_dict_copy)

#note that when we modify the copy it will modify the original one as well

my_dict_copy["email"] = "gmail@email.com"

print(my_dict)
print(my_dict_copy)


# you can also use the built in copy function
#my_dict_copy = my_dict.copy()
my_dict_copy = dict(my_dict) #this way the original dictionary will not get effected

my_dict = {"name":"Max","age":23,"email":"test@email.com"}
my_dict2 = dict(name="Alex",age=28,city="London")

# you can merge both, non existing key values will be added while merging

my_dict.update(my_dict2)
print(my_dict)
 '''
#for the key value pairs you can use only numbers but you have to be careful while
#accessing the elements,
my_dict = {3:9,6:36,7:49}
print(my_dict)
print(my_dict[3])






