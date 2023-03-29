# Strings: ordered, immutable, text representation
'''
my_string = 'Hello world'
print(my_string)

# you can create multiline string by triple quotes
my_str = """
this is the representation of triple quote
you can come up with that


print(my_str)


# you can access the characters inside in string, note that you can not modify
another_string = 'Hello world'
substring = another_string[1:5]
#char = another_string[-2]
print(substring)


greeting = "Hello"
name = "Tom"
sentance = greeting + " " + name 
print(sentance)




#you can iterate over string using loop
# you can name i whatever you want
string = "Hello"
for i in string:
    print(i)

print("-----")

# other way of doing the same thing is list comprehension
[print(i)for i in string]


if "v" in string:
    print("Yes")
else:
    print("No")


you can convert convert every character to upper case or lower case
my_string = "Hello world"
print(my_string.upper())

print(my_string.lower())

# you can check if the string starts with the specific character 
another_str = "Tajikistan"
print(another_str.startswith("T"))

# it will return the index of the searched letter, if it is not there you get -1
print(another_str.find('l'))

#to count the occurance of letter
print(another_str.count('a'))

#to replace the word in a sentance
#if it does not find the string it will not do anything
my_string = "Welcome to Tajikistan"
replaced = my_string.replace('Tajikistan', 'Canada')
print(replaced)

# you can convert the string to the list of elements(words)
my_string = "how are you doing now"
my_list = my_string.split()
print(my_list)
print('\n')

# and you can convert back as well
new_string = ' '.join(my_list)
print(new_string)

#here is one more example

my_list = ['a']* 500000
#print(my_list)

#bad
#since string is immutable, it is not modifying the original list but creating new one
from timeit import default_timer as timer
start = timer()
my_string = ''
for i in my_list:
    my_string +=i
stop = timer()
print("Bad way")
print(stop-start)
# print(my_string)

#good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print("Good way")
print(stop-start)
#print(my_string)

# as you can see if the list gets bigger you can see the difference


# you can format the string with this ways
# %, .format, f-string

var = "Apple"
my_string = "The fruit is %s" % var
print(my_string)


#note %s stands for string, %d stands for integer decimal value, %f is float
# for float if you want to get only two digits after dot, %.2f 
var = "Apple"
my_string = "The fruit is {}".format(var)
print(my_string)
'''
var = "Banana"
my_string = f"The fruit is {var}"
print(my_string)














