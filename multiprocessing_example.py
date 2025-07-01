from multiprocessing import Process
import os

processes = []
num_processes = os.cpu_count()

def squre_numbers():
    for i in range(100):
        i*i

#create processes
for i in range(num_processes):
    p = Process(target=squre_numbers)
    processes.append(p)

# start 
for p in processes:
    p.start()

# join
for p in processes:
    p.join()