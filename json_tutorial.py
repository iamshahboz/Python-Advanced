# 
import json
'''
JSON is short for Java Script Object Notation, and it is a lightway data format that is used 
for data exchange. It is monstly used in web applications so you should be confortable working with that
Python comes with built in json module that makes working with JSON very easy.


# imagine we have a dictionary
import json

person = {"name":"Smith","age":30,"city":"New York","hasChildren":False,"titles":["engineer","programmer"]}
# lets say I want to convert it to a json format
personJSON = json.dumps(person,indent=4,sort_keys=True)
#print(personJSON)

# you can dump it into a file

# with open('person.json','w') as file:
#     json.dump(person,file,indent=4)

# another example is, you have json file and you want to convert it to python object, this process is called deserialization,or decoding

# person = json.loads(personJSON)
# print(person)

# If you want to convert from a json file 
with open('person.json','r') as file:
    person = json.load(file)
    print(person)
    '''

class User:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    
    
user = User('Max',27)
def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name, 'age':o.age,o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user,default=encode_user)
print(userJSON)

