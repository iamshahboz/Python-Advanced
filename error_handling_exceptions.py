# Syntax error: It occurs when the parser detects a syntatically incorrect statement
# a = 5 print(a)

#a = 5
#print(a))

# Even if a statement is syntatically correct it might cause an error when executed
#and it is called exception error

#for instance

#import somemodule 
#this will cause module error

#a = 5
#b = c 

#this will cause name error

# value error: happend if the function or operation recieves an argument
# that has the right type but an inappropriate value

a = [1,2,3]
a.remove(1)

#this works but if we put 4 instead we will get value error

a[6] 
#this will occur index error

my_dict = {
    'name': 'Jack'
}
my_dict['age']
# this will give key error

# If you want to force exception to occur
# x = -5
# if x < 0:
#     raise Exception('x should be positive')

# x = -5
# # the assert statement  will throught an assertion error when your condition is not True
# assert(x >=0 ), 'x is not positive'

try:
    a = 5 / 0
except Exception as e:
    print(e)
    







