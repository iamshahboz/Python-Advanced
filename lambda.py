# Lambda function is a small one line anonymous function,that is defined
# without a name 

# add10 = lambda x: x+10
# print(add10(5))

mult = lambda x,y: x*y
#print(mult(3,5))

a = [1,2,3,4,5,6]
# b = map(lambda x: x*2, a)
# print(list(b))

# you can do the same thing with list comprehension
# c= [x*2 for x in a]
# print(c)

# if we want to return only numbers which are even

c = [x for x in a if x%2==0]
print(c)




