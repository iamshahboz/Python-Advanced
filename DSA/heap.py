

import heapq 

a = [5,7,9,1,3]

heapq.heapify(a)

print('Created heap is:', a)

# Push 4 into heap

heapq.heappush(a, 4)

# printing modified heap
print('Modified heap is: ', a)

# using heap pop to pop smallest element

print('The smallest element is: ', heapq.heappop(a))
