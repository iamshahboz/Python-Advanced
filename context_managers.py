'''
The with statement in Python is quite useful tool for properly managing external resources
in your programs. It allows you to take advantage of existing context managers 
to automatically handle the setup and teardown phrases whenever you're dealing
with external resources or with operations that require those phrases.

'''

# try finally approach

# file = open('hello.txt', 'a')

# try:
#     file.write('\nTHis is new sentance')

# finally:
#     file.close()


# the with statement approach

with open('hello.txt', mode='w') as file:
    file.write('Adding text using with statement')


'''
Opening files using with statement is generally recommended because it 
ensures that open file descriptors are automatically closed after the flow 
of execution leaves the with block code
'''


# using async with statement 

import aiohttp
import asyncio



