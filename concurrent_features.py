
'''
A Process can consist of multiple threads. And this Threads run in the same Process
and share the same memory space.

Two different Processes have their own memory space and they don't share anything.

In a Python program only one Thead can execute at a time even on a multi core machine (by default)

When would you use Threads and when would you use Processes.

Threads are lighter and are good for I/0 bound tasks ex. Network request and db queries.

For image processing and training machine learning models you should use processes.

'''

# Function to compute sum of squares
import time 
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests

# def sum_of_squares(n):
#     return sum(i * i for i in range(n))

# if __name__ == '__main__':
#     numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]

#     start = time.time()
#     results = [sum_of_squares(n) for n in numbers]
#     end = time.time()

#     print('Results',results)
#     print(f'Single thread time: {end-start:.2f} seconds')

# now lets test with process


# def sum_of_squares(n):
#     return sum(i * i for i in range(n))

# if __name__ == '__main__':
#     numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]

#     start = time.time()
#     with ProcessPoolExecutor() as executor:
#         results = list(executor.map(sum_of_squares, numbers))
    
#     end = time.time()

#     print('Results',results)
#     print(f'Single thread time: {end-start:.2f} seconds')

## Now lets see the usage of Thread for I/0 bound tasks



def fetch_url(url):
    response = requests.get(url)
    return f'{url} -> {response.status_code}'

if __name__ == '__main__':
    urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
    ]

start = time.time()

results = [fetch_url(url) for url in urls]


end = time.time()
print(f'Single Threaded time: {end-start:.2f} seconds')

# last_time 8:20


